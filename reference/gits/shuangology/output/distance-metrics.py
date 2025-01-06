"""
Distance Metrics for Financial Analysis.

This module implements various distance and dependency metrics including mutual information,
variation of information, and entropy-based measures.
"""

from typing import Tuple, Optional, Union
import numpy as np
import scipy.stats as ss
from sklearn.metrics import mutual_info_score

def calculate_entropy_metrics(x: np.ndarray, y: np.ndarray, bins: int = 100) -> dict:
    """
    Calculate various entropy-based metrics between two variables.
    
    Args:
        x: First variable
        y: Second variable
        bins: Number of bins for histogram
        
    Returns:
        Dictionary containing entropy metrics
    """
    cXY = np.histogram2d(x, y, bins)[0]
    hX = ss.entropy(np.histogram(x, bins)[0])
    hY = ss.entropy(np.histogram(y, bins)[0])
    iXY = mutual_info_score(None, None, contingency=cXY)
    iXYn = iXY / min(hX, hY)
    hXY = hX + hY - iXY
    hX_Y = hXY - hY
    hY_X = hXY - hX
    
    return {
        'marginal_entropy_x': hX,
        'marginal_entropy_y': hY,
        'mutual_information': iXY,
        'normalized_mutual_information': iXYn,
        'conditional_entropy_x_y': hX_Y,
        'conditional_entropy_y_x': hY_X,
        'joint_entropy': hXY
    }

def variation_information(x: np.ndarray, y: np.ndarray, bins: int, 
                         normalize: bool = False) -> float:
    """
    Calculate variation of information between two variables.
    
    Args:
        x: First variable
        y: Second variable
        bins: Number of bins for histogram
        normalize: Whether to normalize the result
        
    Returns:
        Variation of information value
    """
    cXY = np.histogram2d(x, y, bins)[0]
    iXY = mutual_info_score(None, None, contingency=cXY)
    hX = ss.entropy(np.histogram(x, bins)[0])
    hY = ss.entropy(np.histogram(y, bins)[0])
    vXY = hX + hY - 2 * iXY
    
    if normalize:
        hXY = hX + hY - iXY
        vXY /= hXY
        
    return vXY

def optimal_bin_count(n_obs: int, corr: Optional[float] = None) -> int:
    """
    Calculate optimal number of bins for discretization.
    
    Args:
        n_obs: Number of observations
        corr: Correlation coefficient for bivariate case
        
    Returns:
        Optimal number of bins
    """
    if corr is None:
        z = (8 + 324*n_obs + 12*(36*n_obs + 729*n_obs**2)**0.5)**(1/3.)
        b = round(z/6. + 2./(3*z) + 1./3)
    else:
        if abs(1 - corr**2) < 1e-5:
            corr = np.sign(corr) * (abs(corr) - 1e-5)
        b = round(2**-0.5 * (1 + (1 + 24*n_obs/(1 - corr**2))**0.5)**0.5)
    return int(b)

def variation_information_optimal(x: np.ndarray, y: np.ndarray, 
                                normalize: bool = False) -> float:
    """
    Calculate variation of information using optimal bin count.
    
    Args:
        x: First variable
        y: Second variable
        normalize: Whether to normalize the result
        
    Returns:
        Variation of information value
    """
    bins = optimal_bin_count(x.shape[0], corr=np.corrcoef(x, y)[0, 1])
    return variation_information(x, y, bins, normalize)

def mutual_information(x: np.ndarray, y: np.ndarray, 
                      normalize: bool = False) -> float:
    """
    Calculate mutual information between two variables.
    
    Args:
        x: First variable
        y: Second variable
        normalize: Whether to normalize the result
        
    Returns:
        Mutual information value
    """
    bins = optimal_bin_count(x.shape[0], corr=np.corrcoef(x, y)[0, 1])
    cXY = np.histogram2d(x, y, bins)[0]
    iXY = mutual_info_score(None, None, contingency=cXY)
    
    if normalize:
        hX = ss.entropy(np.histogram(x, bins)[0])
        hY = ss.entropy(np.histogram(y, bins)[0])
        iXY /= min(hX, hY)
        
    return iXY

def generate_correlated_normals(size: int, rho: float, 
                              mu: float = 0, sigma: float = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate correlated normal random variables.
    
    Args:
        size: Number of samples
        rho: Correlation coefficient
        mu: Mean
        sigma: Standard deviation
        
    Returns:
        Tuple of (x, y) correlated variables
    """
    rr = np.random.normal(mu, sigma, size=(2, size))
    x, y_ = rr[0, :], rr[1, :]
    y = rho * x + np.sqrt(1 - rho**2) * y_
    return x, y
