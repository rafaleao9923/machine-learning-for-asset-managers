"""
Enhanced denoising and portfolio optimization with robust implementation.
"""

import numpy as np
import pandas as pd
from scipy import linalg, optimize, cluster
from sklearn.covariance import LedoitWolf, OAS
from numba import njit
from typing import Tuple, List, Optional, Dict
import warnings

def validate_returns(returns: np.ndarray) -> None:
    """Validate returns data."""
    if np.isnan(returns).any():
        raise ValueError("Returns contain NaN values")
    if np.isinf(returns).any():
        raise ValueError("Returns contain infinite values")

def project_to_pd(matrix: np.ndarray, epsilon: float = 1e-8) -> np.ndarray:
    """Project matrix to nearest positive definite matrix."""
    eigvals, eigvecs = linalg.eigh(matrix)
    eigvals = np.maximum(eigvals, epsilon)
    return eigvecs @ np.diag(eigvals) @ eigvecs.T

def factor_model_denoise(returns: np.ndarray, n_factors: Optional[int] = None) -> np.ndarray:
    """
    Denoise using statistical factor model with positive definiteness guarantee.
    """
    T, N = returns.shape
    if n_factors is None:
        n_factors = min(3, N // 3)  # Conservative default
    if n_factors >= min(T, N):
        raise ValueError(f"n_factors ({n_factors}) must be less than min(T,N)={min(T,N)}")
        
    U, s, Vh = linalg.svd(returns, full_matrices=False)
    s[n_factors:] = 0
    denoised_returns = U @ np.diag(s) @ Vh
    cov = denoised_returns.T @ denoised_returns / T
    return project_to_pd(cov)

def adaptive_thresholding(corr: np.ndarray, q: float, method: str = 'power') -> np.ndarray:
    """
    Enhanced adaptive thresholding with multiple methods.
    """
    eigvals, eigvecs = linalg.eigh(corr)
    if method == 'power':
        threshold = (q**0.5 + 1/q**0.5)**2
        weights = np.where(eigvals > threshold, 1.0, 
                         (eigvals/threshold)**2)
    else:  # Linear
        threshold = q**0.5
        weights = np.where(eigvals > threshold, 1.0, 
                         eigvals/threshold)
    
    filtered = eigvals * weights
    denoised = eigvecs @ np.diag(filtered) @ eigvecs.T
    return project_to_pd(denoised)

def shrinkage_ensemble(returns: np.ndarray, 
                      lookback: int = 252) -> np.ndarray:
    """
    Adaptive shrinkage ensemble based on out-of-sample performance.
    """
    if len(returns) < lookback:
        raise ValueError("Insufficient data for lookback period")
        
    def get_risk(est: np.ndarray, test_rets: np.ndarray) -> float:
        w = np.ones(est.shape[0]) / est.shape[0]  # Equal weights
        return np.sqrt(w @ est @ w) - np.std(test_rets @ w)
    
    # Calculate weights based on historical performance
    lw = LedoitWolf()
    oas = OAS()
    lw_errors = []
    oas_errors = []
    
    for t in range(lookback, len(returns), lookback//4):
        train = returns[t-lookback:t]
        test = returns[t:t+lookback//4]
        
        lw.fit(train)
        oas.fit(train)
        
        lw_errors.append(abs(get_risk(lw.covariance_, test)))
        oas_errors.append(abs(get_risk(oas.covariance_, test)))
    
    # Compute adaptive weights
    lw_weight = 1 / (1 + np.mean(lw_errors))
    oas_weight = 1 / (1 + np.mean(oas_errors))
    total = lw_weight + oas_weight
    
    # Final estimation
    lw.fit(returns)
    oas.fit(returns)
    return (lw_weight * lw.covariance_ + 
            oas_weight * oas.covariance_) / total

def hierarchical_risk_parity(cov: np.ndarray) -> np.ndarray:
    """
    Hierarchical Risk Parity using proper clustering.
    """
    corr = cov / np.sqrt(np.outer(np.diag(cov), np.diag(cov)))
    dist = np.sqrt(2 * (1 - corr))
    
    # Hierarchical clustering
    linkage = cluster.hierarchy.linkage(dist, method='single')
    sort_ix = cluster.hierarchy.leaves_list(linkage)
    
    # Sort covariance by cluster order
    cov = cov[sort_ix][:,sort_ix]
    
    # Recursive bisection
    def bisect(cov: np.ndarray, sort_ix: np.ndarray) -> np.ndarray:
        if len(sort_ix) == 1:
            return np.array([1.])
        
        mid = len(sort_ix) // 2
        left_ix = sort_ix[:mid]
        right_ix = sort_ix[mid:]
        
        # Recursive weights
        left_w = bisect(cov[left_ix][:,left_ix], left_ix)
        right_w = bisect(cov[right_ix][:,right_ix], right_ix)
        
        # Combine weights
        left_risk = np.sqrt(left_w @ cov[left_ix][:,left_ix] @ left_w)
        right_risk = np.sqrt(right_w @ cov[right_ix][:,right_ix] @ right_w)
        factor = 1 / (left_risk + right_risk)
        
        return np.concatenate([
            left_w * factor * left_risk,
            right_w * factor * right_risk
        ])
    
    weights = bisect(cov, np.arange(len(cov)))
    
    # Reorder weights to original order
    inv_sort_ix = np.argsort(sort_ix)
    return weights[inv_sort_ix]

def risk_parity_portfolio(cov: np.ndarray, 
                         tol: float = 1e-12) -> np.ndarray:
    """
    Risk parity with gradient information and robust optimization.
    """
    n = len(cov)
    
    def obj_func(w: np.ndarray) -> Tuple[float, np.ndarray]:
        w = w.reshape(-1,1)
        risk = np.sqrt(w.T @ cov @ w)
        risk_contrib = w * (cov @ w) / risk
        grad = cov @ w / risk - risk_contrib / w / risk
        return np.std(risk_contrib), grad.flatten()
    
    # Initialize with equal risk contribution
    x0 = np.ones(n) / np.sqrt(np.diag(cov))
    x0 /= x0.sum()
    
    # Optimization constraints
    constraints = [
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
        {'type': 'ineq', 'fun': lambda x: x}  # Non-negative weights
    ]
    
    try:
        result = optimize.minimize(
            lambda w: obj_func(w)[0],
            x0,
            jac=lambda w: obj_func(w)[1],
            method='SLSQP',
            constraints=constraints,
            bounds=[(0, 1)] * n,
            options={'ftol': tol, 'maxiter': 1000}
        )
        if not result.success:
            warnings.warn(f"Optimization failed: {result.message}")
        return np.clip(result.x, 0, 1)
    except:
        warnings.warn("Optimization failed, returning equal weights")
        return np.ones(n) / n

class PortfolioOptimizer:
    """Enhanced portfolio optimization with robust implementation."""
    
    def __init__(self, returns: np.ndarray):
        validate_returns(returns)
        self.returns = returns
        self.T, self.N = returns.shape
        self.q = self.T / self.N
        
    def denoise_covariance(self, method: str = 'factor', 
                          **kwargs) -> np.ndarray:
        """Denoising with expanded options and error handling."""
        try:
            if method == 'factor':
                return factor_model_denoise(self.returns, **kwargs)
            elif method == 'shrinkage':
                return shrinkage_ensemble(self.returns, **kwargs)
            elif method == 'adaptive':
                sample_cov = np.cov(self.returns, rowvar=False)
                sample_corr = sample_cov / np.sqrt(
                    np.outer(np.diag(sample_cov), np.diag(sample_cov)))
                denoised_corr = adaptive_thresholding(
                    sample_corr, self.q, **kwargs)
                std = np.sqrt(np.diag(sample_cov))
                return project_to_pd(denoised_corr * np.outer(std, std))
            else:
                raise ValueError(f"Unknown method: {method}")
        except Exception as e:
            warnings.warn(f"Denoising failed: {str(e)}. Using sample covariance.")
            return np.cov(self.returns, rowvar=False)
    
    def optimize_portfolio(self, method: str = 'hrp', 
                         denoising: str = 'factor', 
                         **kwargs) -> np.ndarray:
        """Portfolio optimization with enhanced error handling."""
        try:
            cov = self.denoise_covariance(denoising, **kwargs)
            
            if method == 'hrp':
                return hierarchical_risk_parity(cov)
            elif method == 'min_corr':
                corr = cov / np.sqrt(np.outer(np.diag(cov), np.diag(cov)))
                w = minimum_correlation_portfolio(corr)
                return np.clip(w, 0, 1)  # Ensure valid weights
            elif method == 'risk_parity':
                return risk_parity_portfolio(cov, **kwargs)
            else:
                raise ValueError(f"Unknown method: {method}")
        except Exception as e:
            warnings.warn(f"Optimization failed: {str(e)}. Using equal weights.")
            return np.ones(self.N) / self.N
    
    def backtest_portfolio(self, method: str = 'hrp',
                          denoising: str = 'factor',
                          lookback: int = 252,
                          rebalance_freq: int = 21,
                          **kwargs) -> pd.DataFrame:
        """Enhanced backtesting with performance metrics."""
        results = []
        weights_history = []
        
        for t in range(lookback, len(self.returns), rebalance_freq):
            window = self.returns[t-lookback:t]
            weights = self.optimize_portfolio(
                method, denoising, **kwargs)
            weights_history.append(weights)
            
            # Forward returns
            fwd_rets = self.returns[t:t+rebalance_freq]
            port_rets = fwd_rets @ weights
            
            results.append(pd.DataFrame({
                'returns': port_rets,
                'cumulative': (1 + port_rets).cumprod(),
                'drawdown': 1 - (1 + port_rets).cumprod() / \
                    (1 + port_rets).cumprod().cummax()
            }, index=pd.RangeIndex(t, t+len(port_rets))))
        
        results_df = pd.concat(results)
        
        # Add performance metrics
        ann_ret = results_df['returns'].mean() * 252
        ann_vol = results_df['returns'].std() * np.sqrt(252)
        sharpe = ann_ret / ann_vol
        max_dd = results_df['drawdown'].max()
        
        print(f"\nPerformance Metrics:")
        print(f"Annual Return: {ann_ret:.2%}")
        print(f"Annual Volatility: {ann_vol:.2%}")
        print(f"Sharpe Ratio: {sharpe:.2f}")
        print(f"Maximum Drawdown: {max_dd:.2%}")
        
        return results_df