"""
Advanced methods for denoising financial covariance matrices and portfolio optimization.

This module implements the Marcenko-Pastur theorem and various denoising techniques
for financial analysis, with optimized performance and robust error handling.
"""

from typing import Tuple, Optional, Union, Any
import warnings
import numpy as np
import pandas as pd
from scipy import linalg
from scipy.optimize import minimize
from sklearn.covariance import LedoitWolf
from sklearn.neighbors import KernelDensity

# Default parameters
DEFAULT_BANDWIDTH = 0.25
DEFAULT_ALPHA = 0.5
DEFAULT_POINTS = 1000
DEFAULT_Q = 10
MIN_EIGENVAL = 1e-8


def validate_matrix(matrix: np.ndarray) -> None:
    """Validate matrix properties."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("Input must be numpy array")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")
    if not np.allclose(matrix, matrix.T):
        raise ValueError("Matrix must be symmetric")


def mpPDF(variance: float, q: float, points: int = DEFAULT_POINTS) -> pd.Series:
    """Calculate Marcenko-Pastur probability density function."""
    if variance <= 0 or q <= 0:
        raise ValueError("Variance and q must be positive")

    eMin = variance * (1 - (1/q)**0.5)**2
    eMax = variance * (1 + (1/q)**0.5)**2
    eVal = np.linspace(eMin, eMax, points)
    pdf = q/(2 * np.pi * variance * eVal) * \
        ((eMax - eVal) * (eVal - eMin))**0.5
    return pd.Series(pdf, index=eVal)


def getPCA(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Perform PCA with robust eigenvalue computation."""
    validate_matrix(matrix)
    try:
        eVal, eVec = linalg.eigh(matrix)
        if np.any(eVal < -MIN_EIGENVAL):
            warnings.warn("Matrix has significant negative eigenvalues")
        indices = eVal.argsort()[::-1]
        return np.diagflat(eVal[indices]), eVec[:, indices]
    except linalg.LinAlgError:
        raise ValueError("Failed to compute eigendecomposition")


def fitKDE(obs: np.ndarray, bandwidth: float = DEFAULT_BANDWIDTH,
           kernel: str = 'gaussian', x: Optional[np.ndarray] = None) -> pd.Series:
    """Fit kernel density estimation with vectorized operations."""
    obs = np.asarray(obs).reshape(-1, 1)
    x = np.unique(obs) if x is None else np.asarray(x).reshape(-1, 1)

    kde = KernelDensity(kernel=kernel, bandwidth=bandwidth).fit(obs)
    logProb = kde.score_samples(x)
    return pd.Series(np.exp(logProb), index=x.flatten())


def getRndCov(n_cols: int, n_facts: int) -> np.ndarray:
    """Generate random covariance matrix using efficient operations."""
    if n_cols <= 0 or n_facts <= 0:
        raise ValueError("Dimensions must be positive")

    w = np.random.normal(size=(n_cols, n_facts))
    cov = np.einsum('ik,jk->ij', w, w)
    cov += np.diag(np.random.uniform(size=n_cols))
    return cov


def cov2corr(cov: np.ndarray) -> np.ndarray:
    """Convert covariance to correlation matrix using vectorized operations."""
    validate_matrix(cov)
    std = np.sqrt(np.diag(cov))
    if np.any(std < MIN_EIGENVAL):
        raise ValueError("Near-zero standard deviations detected")

    corr = cov / np.outer(std, std)
    np.clip(corr, -1, 1, out=corr)
    return corr


def corr2cov(corr: np.ndarray, std: np.ndarray) -> np.ndarray:
    """Convert correlation to covariance matrix with validation."""
    validate_matrix(corr)
    if np.any(std < MIN_EIGENVAL):
        raise ValueError("Invalid standard deviations")

    cov = np.einsum('i,ij,j->ij', std, corr, std)
    return cov


def errPDFs(params: np.ndarray, eVal: np.ndarray, q: float,
            bandwidth: float, points: int = DEFAULT_POINTS) -> float:
    """Calculate PDF fitting error with optimized operations."""
    variance = params[0]
    if variance <= 0:
        return np.inf

    pdf0 = mpPDF(variance, q, points)
    pdf1 = fitKDE(eVal, bandwidth, x=pdf0.index.values)
    return np.sum((pdf1 - pdf0)**2)


def findMaxEval(eVal: np.ndarray, q: float, bandwidth: float) -> Tuple[float, float]:
    """Find maximum eigenvalue with robust optimization."""
    result = minimize(
        errPDFs,
        x0=[0.5],
        args=(eVal, q, bandwidth),
        method='trust-constr',
        bounds=[(MIN_EIGENVAL, 1-MIN_EIGENVAL)],
        options={'gtol': 1e-6}
    )

    if not result.success:
        warnings.warn("Optimization failed to converge")

    variance = result.x[0]
    return variance * (1 + (1./q)**0.5)**2, variance


def _denoise_base(eVal: np.ndarray, eVec: np.ndarray, n_facts: int,
                  method: str = 'constant', alpha: float = DEFAULT_ALPHA) -> np.ndarray:
    """Base denoising implementation for both methods."""
    if method == 'constant':
        eVal_new = np.diag(eVal).copy()
        eVal_new[n_facts:] = eVal_new[n_facts:].mean()
        return np.einsum('ij,j,kj->ik', eVec, eVal_new, eVec)
    elif method == 'shrinkage':
        eValL, eVecL = eVal[:n_facts, :n_facts], eVec[:, :n_facts]
        eValR, eVecR = eVal[n_facts:, n_facts:], eVec[:, n_facts:]
        corr0 = np.einsum('ij,jk,lj->il', eVecL, eValL, eVecL)
        corr1 = np.einsum('ij,jk,lj->il', eVecR, eValR, eVecR)
        return corr0 + alpha * corr1 + (1 - alpha) * np.diag(np.diag(corr1))
    else:
        raise ValueError("Invalid denoising method")


def denoisedCorr(eVal: np.ndarray, eVec: np.ndarray, n_facts: int) -> np.ndarray:
    """Denoise correlation matrix using constant residual method."""
    corr = _denoise_base(eVal, eVec, n_facts, method='constant')
    return cov2corr(corr)


def denoisedCorr2(eVal: np.ndarray, eVec: np.ndarray, n_facts: int,
                  alpha: float = DEFAULT_ALPHA) -> np.ndarray:
    """Denoise correlation matrix using targeted shrinkage."""
    return _denoise_base(eVal, eVec, n_facts, method='shrinkage', alpha=alpha)


def formBlockMatrix(n_blocks: int, block_size: int, block_corr: float) -> np.ndarray:
    """Form block correlation matrix with validation."""
    if not (0 <= block_corr <= 1):
        raise ValueError("Block correlation must be between 0 and 1")

    block = np.full((block_size, block_size), block_corr)
    np.fill_diagonal(block, 1)
    return linalg.block_diag(*([block] * n_blocks))


def optPort(cov: np.ndarray, mu: Optional[np.ndarray] = None) -> np.ndarray:
    """Calculate optimal portfolio weights using robust solver."""
    validate_matrix(cov)
    n = cov.shape[0]
    ones = np.ones((n, 1))
    mu = ones if mu is None else mu.reshape(-1, 1)

    try:
        w = linalg.solve(cov, mu, assume_a='sym')
        return w / (ones.T @ w)
    except linalg.LinAlgError:
        raise ValueError("Singular covariance matrix detected")


def simCovMu(mu0: np.ndarray, cov0: np.ndarray, n_obs: int,
             shrink: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """Simulate covariance matrix and means with validation."""
    validate_matrix(cov0)

    try:
        x = np.random.multivariate_normal(mu0.flatten(), cov0, size=n_obs)
        mu1 = x.mean(axis=0).reshape(-1, 1)
        cov1 = LedoitWolf().fit(x).covariance_ if shrink else np.cov(x, rowvar=0)
        return mu1, cov1
    except (ValueError, np.linalg.LinAlgError) as e:
        raise ValueError(f"Simulation failed: {str(e)}")
