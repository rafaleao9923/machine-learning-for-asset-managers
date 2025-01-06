import numpy as np
import pandas as pd
import statsmodels.api as sm
# from scipy import stats
from statsmodels.tsa.stattools import adfuller
from concurrent.futures import ThreadPoolExecutor
from typing import Tuple, List

def t_value_linear_trend(close: np.ndarray) -> float:
    """Calculate t-value for linear trend."""
    x = np.column_stack((np.ones(len(close)), np.arange(len(close))))
    return sm.OLS(close, x).fit().tvalues[1]

def polynomial_trend(close: np.ndarray, degree: int = 2) -> float:
    """Calculate polynomial trend t-value."""
    x = np.arange(len(close))
    coeffs = np.polyfit(x, close, degree)
    y_pred = np.polyval(coeffs, x)
    residuals = close - y_pred
    mse = np.sum(residuals**2) / (len(close) - degree - 1)
    return coeffs[0] / np.sqrt(mse)

def rolling_mean_test(close: np.ndarray, window: int = 20) -> float:
    """Perform rolling mean trend test."""
    if len(close) < window * 2:
        return 0
    first_half = close[:window].mean()
    second_half = close[-window:].mean()
    pooled_std = np.sqrt(np.var(close[:window], ddof=1)/window + 
                        np.var(close[-window:], ddof=1)/window)
    return (second_half - first_half) / pooled_std if pooled_std != 0 else 0

def get_trend_labels(molecule: pd.DatetimeIndex, close: pd.Series, 
                    span: Tuple[int, int], 
                    methods: List[str] = ['linear', 'poly', 'rolling', 'adf']) -> pd.DataFrame:
    """Get trend labels using multiple methods."""
    out = pd.DataFrame(index=molecule, 
                      columns=['t1', 'tVal', 'bin', 'poly_trend', 'rolling_trend', 'adf_trend'])
    hrzns = range(*span)
    
    def process_date(dt0):
        iloc0 = close.index.get_loc(dt0)
        if iloc0 + max(hrzns) > len(close):
            return None
            
        results = {}
        for hrzn in hrzns:
            dt1 = close.index[iloc0 + hrzn - 1]
            subset = close[dt0:dt1].values
            
            if len(subset) < 2:
                continue
                
            results[dt1] = {
                'linear': t_value_linear_trend(subset),
                'poly': polynomial_trend(subset),
                'rolling': rolling_mean_test(subset),
                'adf': -adfuller(subset)[0]  # Negative ADF stat for consistency
            }
        
        if not results:
            return None
            
        # Aggregate results for each method
        method_results = {method: pd.Series({dt: res[method] 
                         for dt, res in results.items()})
                         for method in ['linear', 'poly', 'rolling', 'adf']}
        
        max_dt = max(method_results['linear'].abs().idxmax(),
                    method_results['poly'].abs().idxmax())
        
        return pd.Series({
            't1': max_dt,
            'tVal': method_results['linear'].loc[max_dt],
            'bin': np.sign(method_results['linear'].loc[max_dt]),
            'poly_trend': method_results['poly'].loc[max_dt],
            'rolling_trend': method_results['rolling'].loc[max_dt],
            'adf_trend': method_results['adf'].loc[max_dt]
        })

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_date, molecule))
    
    for dt0, result in zip(molecule, results):
        if result is not None:
            out.loc[dt0] = result
    
    out['t1'] = pd.to_datetime(out['t1'])
    out['bin'] = out['bin'].astype('int8')
    return out.dropna(subset=['bin'])

def plot_trend_labels(close: pd.Series, labels: pd.DataFrame, title: str):
    """Plot trend labels with multiple indicators."""
    import matplotlib.pyplot as plt
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Price and linear trend
    scatter = ax1.scatter(labels.index, close.loc[labels.index], 
                         c=labels['bin'], cmap='viridis')
    ax1.plot(close.index, close.values, color='gray', alpha=0.5)
    ax1.set_title(f'{title} - Price and Linear Trend')
    
    # Trend indicators
    for col, color in zip(['poly_trend', 'rolling_trend', 'adf_trend'], 
                         ['blue', 'green', 'red']):
        ax2.plot(labels.index, labels[col], 
                label=col.replace('_', ' ').title(), 
                color=color, alpha=0.7)
    
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.3)
    ax2.legend()
    ax2.set_title('Trend Indicators')
    
    plt.tight_layout()
    return fig, (ax1, ax2)