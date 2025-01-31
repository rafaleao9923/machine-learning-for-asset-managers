"""
Distance Metrics for Financial Analysis.

This module implements various distance and dependency metrics including mutual information,
variation of information, and entropy-based measures with improved numerical stability
and error handling.
"""

from typing import Tuple, Optional, Union, Dict
from dataclasses import dataclass
import numpy as np
import scipy.stats as ss
from sklearn.metrics import mutual_info_score

EPSILON = 1e-10  # Small constant for numerical stability

@dataclass
class EntropyMetrics:
    """Container for entropy-based metrics."""
    marginal_entropy_x: float
    marginal_entropy_y: float
    mutual_information: float
    normalized_mutual_information: float
    conditional_entropy_x_y: float
    conditional_entropy_y_x: float
    joint_entropy: float

def validate_inputs(x: np.ndarray, y: np.ndarray) -> None:
    """Validate input arrays for calculations."""
    if x.size == 0 or y.size == 0:
        raise ValueError("Input arrays cannot be empty")
    if x.size != y.size:
        raise ValueError("Input arrays must have same length")
    if np.any(np.isnan(x)) or np.any(np.isnan(y)):
        raise ValueError("Input arrays contain NaN values")
    if np.any(np.isinf(x)) or np.any(np.isinf(y)):
        raise ValueError("Input arrays contain infinite values")

def compute_histogram(x: np.ndarray, bins: int) -> Tuple[np.ndarray, np.ndarray]:
    """Compute histogram with optimal bin edges."""
    hist, edges = np.histogram(x, bins=bins)
    hist = hist.astype(float) + EPSILON  # Avoid zero counts
    hist /= hist.sum()  # Normalize
    return hist, edges

def compute_entropy(hist: np.ndarray) -> float:
    """Compute entropy from histogram."""
    return ss.entropy(hist)

def compute_joint_histogram(x: np.ndarray, y: np.ndarray, 
                          bins: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute 2D histogram with optimal bin edges."""
    hist, x_edges, y_edges = np.histogram2d(x, y, bins=bins)
    hist = hist.astype(float) + EPSILON
    hist /= hist.sum()
    return hist, x_edges, y_edges

def optimal_bin_count(n_obs: int, corr: Optional[float] = None) -> int:
    """
    Calculate optimal number of bins for discretization using established rules.
    
    Args:
        n_obs: Number of observations
        corr: Correlation coefficient for bivariate case
        
    Returns:
        Optimal number of bins
        
    Raises:
        ValueError: If correlation is invalid or observations count is too low
    """
    if n_obs < 2:
        raise ValueError("Need at least 2 observations")
        
    if corr is None:
        # Freedman-Diaconis rule for univariate case
        z = (8 + 324*n_obs + 12*(36*n_obs + 729*n_obs**2)**0.5)**(1/3.)
        b = round(z/6. + 2./(3*z) + 1./3)
    else:
        # Handle edge cases for correlation
        if abs(corr) > 1:
            raise ValueError("Correlation must be between -1 and 1")
        if abs(1 - corr**2) < EPSILON:
            corr = np.sign(corr) * (1 - EPSILON)
        # Modified rule for bivariate case
        b = round(2**-0.5 * (1 + (1 + 24*n_obs/(1 - corr**2))**0.5)**0.5)
    
    return max(int(b), 2)  # Ensure at least 2 bins

def calculate_entropy_metrics(x: np.ndarray, y: np.ndarray, 
                            bins: Optional[int] = None) -> EntropyMetrics:
    """
    Calculate comprehensive entropy-based metrics between two variables.
    
    Args:
        x: First variable
        y: Second variable
        bins: Number of bins (if None, calculated optimally)
        
    Returns:
        EntropyMetrics object containing all metrics
        
    Raises:
        ValueError: For invalid inputs
    """
    validate_inputs(x, y)
    
    if bins is None:
        bins = optimal_bin_count(x.size, np.corrcoef(x, y)[0, 1])
    
    # Compute histograms
    hist_x, _ = compute_histogram(x, bins)
    hist_y, _ = compute_histogram(y, bins)
    joint_hist, _, _ = compute_joint_histogram(x, y, bins)
    
    # Calculate entropy metrics
    hX = compute_entropy(hist_x)
    hY = compute_entropy(hist_y)
    iXY = mutual_info_score(None, None, contingency=joint_hist)
    
    # Handle edge case where both entropies are near zero
    min_entropy = min(hX, hY)
    if min_entropy < EPSILON:
        iXYn = 0.0
    else:
        iXYn = iXY / min_entropy
    
    hXY = hX + hY - iXY
    hX_Y = hXY - hY
    hY_X = hXY - hX
    
    return EntropyMetrics(
        marginal_entropy_x=float(hX),
        marginal_entropy_y=float(hY),
        mutual_information=float(iXY),
        normalized_mutual_information=float(iXYn),
        conditional_entropy_x_y=float(hX_Y),
        conditional_entropy_y_x=float(hY_X),
        joint_entropy=float(hXY)
    )

def variation_information(x: np.ndarray, y: np.ndarray, 
                         bins: Optional[int] = None,
                         normalize: bool = False) -> float:
    """
    Calculate variation of information between two variables.
    
    Args:
        x: First variable
        y: Second variable
        bins: Number of bins (if None, calculated optimally)
        normalize: Whether to normalize the result
        
    Returns:
        Variation of information value
        
    Raises:
        ValueError: For invalid inputs
    """
    metrics = calculate_entropy_metrics(x, y, bins)
    vXY = metrics.marginal_entropy_x + metrics.marginal_entropy_y - 2 * metrics.mutual_information
    
    if normalize and metrics.joint_entropy > EPSILON:
        vXY /= metrics.joint_entropy
        
    return float(vXY)

def mutual_information(x: np.ndarray, y: np.ndarray,
                      bins: Optional[int] = None,
                      normalize: bool = False) -> float:
    """
    Calculate mutual information between two variables.
    
    Args:
        x: First variable
        y: Second variable
        bins: Number of bins (if None, calculated optimally)
        normalize: Whether to normalize the result
        
    Returns:
        Mutual information value
        
    Raises:
        ValueError: For invalid inputs
    """
    metrics = calculate_entropy_metrics(x, y, bins)
    if normalize:
        return float(metrics.normalized_mutual_information)
    return float(metrics.mutual_information)

def generate_correlated_normals(size: int, rho: float,
                              mu: float = 0, sigma: float = 1,
                              random_state: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate correlated normal random variables.
    
    Args:
        size: Number of samples
        rho: Correlation coefficient
        mu: Mean
        sigma: Standard deviation
        random_state: Random seed for reproducibility
        
    Returns:
        Tuple of (x, y) correlated variables
        
    Raises:
        ValueError: If parameters are invalid
    """
    if abs(rho) > 1:
        raise ValueError("Correlation coefficient must be between -1 and 1")
    if sigma <= 0:
        raise ValueError("Standard deviation must be positive")
    if size < 1:
        raise ValueError("Size must be positive")
        
    if random_state is not None:
        np.random.seed(random_state)
        
    rr = np.random.normal(mu, sigma, size=(2, size))
    x, y_ = rr[0, :], rr[1, :]
    y = rho * x + np.sqrt(1 - rho**2) * y_
    
    return x, y

def compute_distance_matrix(data: np.ndarray,
                          metric: str = 'variation_information',
                          normalize: bool = False) -> np.ndarray:
    """
    Compute pairwise distance matrix using specified metric.
    
    Args:
        data: Matrix where each column is a variable
        metric: Distance metric to use ('variation_information' or 'mutual_information')
        normalize: Whether to normalize the results
        
    Returns:
        Distance matrix
        
    Raises:
        ValueError: For invalid inputs or unknown metric
    """
    if data.ndim != 2:
        raise ValueError("Input must be 2D array")
    if metric not in ['variation_information', 'mutual_information']:
        raise ValueError("Unknown metric")
        
    n = data.shape[1]
    dist_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1, n):
            if metric == 'variation_information':
                dist = variation_information(data[:, i], data[:, j], normalize=normalize)
            else:
                dist = mutual_information(data[:, i], data[:, j], normalize=normalize)
            dist_matrix[i, j] = dist_matrix[j, i] = dist
            
    return dist_matrix