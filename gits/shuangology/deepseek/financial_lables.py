import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.stattools import adfuller
from concurrent.futures import ProcessPoolExecutor
from typing import Tuple, List, Optional, Dict
from functools import lru_cache
from numba import jit
import matplotlib.pyplot as plt
from dataclasses import dataclass
from scipy.stats import norm

@dataclass
class TrendResult:
    """Data class for storing trend analysis results."""
    t_value: float
    confidence_interval: Tuple[float, float]
    trend_strength: float

class AdaptiveWindow:
    """Adaptive window size based on volatility."""
    def __init__(self, min_window: int = 10, max_window: int = 50):
        self.min_window = min_window
        self.max_window = max_window
    
    def get_window(self, data: np.ndarray) -> int:
        """Calculate adaptive window size based on volatility."""
        volatility = np.std(np.diff(data))
        # Scale window size inversely with volatility
        window = int(self.max_window / (1 + volatility))
        return max(self.min_window, min(window, self.max_window))

@jit(nopython=True)
def fast_rolling_stats(data: np.ndarray, window: int) -> Tuple[np.ndarray, np.ndarray]:
    """Optimized rolling mean and std calculation using Numba."""
    n = len(data)
    means = np.zeros(n - window + 1)
    stds = np.zeros(n - window + 1)
    
    for i in range(n - window + 1):
        window_data = data[i:i+window]
        means[i] = np.mean(window_data)
        stds[i] = np.std(window_data)
    
    return means, stds

@lru_cache(maxsize=1024)
def cached_t_value_linear_trend(close_tuple: Tuple[float, ...]) -> TrendResult:
    """Cached version of t-value calculation with confidence intervals."""
    close = np.array(close_tuple)
    x = np.column_stack((np.ones(len(close)), np.arange(len(close))))
    model = sm.OLS(close, x).fit()
    
    t_value = model.tvalues[1]
    conf_int = model.conf_int(alpha=0.05)[1]
    trend_strength = abs(t_value) / np.sqrt(len(close))
    
    return TrendResult(t_value, conf_int, trend_strength)

@jit(nopython=True)
def fast_polynomial_trend(close: np.ndarray, degree: int = 2) -> float:
    """Optimized polynomial trend calculation using Numba."""
    x = np.arange(len(close))
    coeffs = np.polyfit(x, close, degree)
    y_pred = np.polyval(coeffs, x)
    residuals = close - y_pred
    mse = np.sum(residuals**2) / (len(close) - degree - 1)
    return coeffs[0] / np.sqrt(mse)

class TrendAnalyzer:
    """Main class for trend analysis with caching and adaptive windows."""
    def __init__(self, cache_size: int = 1024):
        self.cache_size = cache_size
        self.adaptive_window = AdaptiveWindow()
        self._clear_cache()
    
    def _clear_cache(self):
        """Clear all internal caches."""
        cached_t_value_linear_trend.cache_clear()
    
    def analyze_trend(self, close: np.ndarray) -> Dict[str, TrendResult]:
        """Comprehensive trend analysis with multiple methods."""
        window = self.adaptive_window.get_window(close)
        close_tuple = tuple(close)  # For caching
        
        results = {
            'linear': cached_t_value_linear_trend(close_tuple),
            'poly': TrendResult(
                fast_polynomial_trend(close),
                (-np.inf, np.inf),  # Placeholder for now
                abs(fast_polynomial_trend(close)) / np.sqrt(len(close))
            )
        }
        
        # Add rolling analysis if enough data
        if len(close) >= window * 2:
            means, stds = fast_rolling_stats(close, window)
            z_stat, p_value = stats.ranksums(means[:window], means[-window:])
            conf_int = norm.interval(0.95, loc=z_stat, scale=np.sqrt(1/window))
            results['rolling'] = TrendResult(z_stat, conf_int, abs(z_stat))
        
        return results

def get_trend_labels(
    molecule: pd.DatetimeIndex,
    close: pd.Series,
    span: Tuple[int, int],
    confidence_level: float = 0.95
) -> pd.DataFrame:
    """Enhanced trend labeling with confidence intervals and adaptive windows."""
    analyzer = TrendAnalyzer()
    out = pd.DataFrame(index=molecule, 
                      columns=['t1', 'tVal', 'bin', 'confidence_lower', 
                              'confidence_upper', 'trend_strength'])
    
    def process_date(dt0):
        iloc0 = close.index.get_loc(dt0)
        if iloc0 + span[1] > len(close):
            return None
        
        results = {}
        for hrzn in range(*span):
            dt1 = close.index[iloc0 + hrzn - 1]
            subset = close[dt0:dt1].values
            
            if len(subset) < 2:
                continue
            
            trend_results = analyzer.analyze_trend(subset)
            
            # Combine results using weighted ensemble
            weights = {'linear': 0.4, 'poly': 0.3, 'rolling': 0.3}
            combined_t = sum(res.t_value * weights.get(method, 0) 
                           for method, res in trend_results.items())
            
            confidence_intervals = [res.confidence_interval 
                                 for res in trend_results.values() 
                                 if res.confidence_interval != (-np.inf, np.inf)]
            
            # Aggregate confidence intervals
            if confidence_intervals:
                conf_lower = np.mean([ci[0] for ci in confidence_intervals])
                conf_upper = np.mean([ci[1] for ci in confidence_intervals])
            else:
                conf_lower = conf_upper = np.nan
            
            trend_strength = np.mean([res.trend_strength 
                                    for res in trend_results.values()])
            
            results[dt1] = {
                't_value': combined_t,
                'conf_lower': conf_lower,
                'conf_upper': conf_upper,
                'trend_strength': trend_strength
            }
        
        if not results:
            return None
        
        max_dt = max(results.items(), key=lambda x: abs(x[1]['t_value']))[0]
        max_result = results[max_dt]
        
        return pd.Series({
            't1': max_dt,
            'tVal': max_result['t_value'],
            'bin': np.sign(max_result['t_value']),
            'confidence_lower': max_result['conf_lower'],
            'confidence_upper': max_result['conf_upper'],
            'trend_strength': max_result['trend_strength']
        })
    
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_date, molecule))
    
    for dt0, result in zip(molecule, results):
        if result is not None:
            out.loc[dt0] = result
    
    out['t1'] = pd.to_datetime(out['t1'])
    out['bin'] = out['bin'].astype('int8')
    return out.dropna(subset=['bin'])

def plot_trend_labels(close: pd.Series, labels: pd.DataFrame, title: str):
    """Enhanced visualization with confidence intervals and trend strength."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
    
    # Price and trend direction
    scatter = ax1.scatter(labels.index, close.loc[labels.index],
                         c=labels['bin'], cmap='viridis',
                         s=labels['trend_strength'] * 50)  # Size by strength
    ax1.plot(close.index, close.values, color='gray', alpha=0.5)
    ax1.set_title(f'{title} - Price and Trend Direction')
    
    # T-values with confidence intervals
    ax2.fill_between(labels.index, 
                    labels['confidence_lower'],
                    labels['confidence_upper'],
                    alpha=0.2, color='gray')
    ax2.plot(labels.index, labels['tVal'], color='blue')
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.3)
    ax2.set_title('T-Values with Confidence Intervals')
    
    # Trend strength
    ax3.plot(labels.index, labels['trend_strength'], color='red')
    ax3.fill_between(labels.index, 0, labels['trend_strength'], alpha=0.2)
    ax3.set_title('Trend Strength')
    
    plt.tight_layout()
    return fig, (ax1, ax2, ax3)