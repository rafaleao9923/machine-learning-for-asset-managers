"""
Denoising and Detoning Functions for Financial Analysis.

This module provides implementations of the Marcenko-Pastur theorem and various
denoising methods for financial covariance matrices, along with portfolio optimization utilities.
"""

from typing import Tuple, Optional, List, Union
import numpy as np
import pandas as pd
from scipy.linalg import block_diag
from scipy.optimize import minimize
from sklearn.covariance import LedoitWolf
from sklearn.neighbors import KernelDensity


def mpPDF(var: float, q: float, pts: int = 1000) -> pd.Series:
    """
    Calculate Marcenko-Pastur probability density function.

    Args:
        var: Variance parameter
        q: Ratio T/N (time samples / variables)
        pts: Number of points for PDF calculation

    Returns:
        PDF values as pandas Series
    """
    eMin, eMax = var * (1 - (1/q)**0.5)**2, var * (1 + (1/q)**0.5)**2
    eVal = np.linspace(eMin, eMax, pts)
    pdf = q/(2 * np.pi * var * eVal) * ((eMax - eVal) * (eVal - eMin))**0.5
    return pd.Series(pdf, index=eVal)


def getPCA(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Perform PCA on a given matrix.

    Args:
        matrix: Input matrix for PCA

    Returns:
        Tuple of (eigenvalues matrix, eigenvectors matrix)
    """
    eVal, eVec = np.linalg.eigh(matrix)
    indices = eVal.argsort()[::-1]
    eVal, eVec = eVal[indices], eVec[:, indices]
    eVal = np.diagflat(eVal)
    return eVal, eVec


def fitKDE(obs: np.ndarray, bWidth: float = 0.25, kernel: str = 'gaussian',
           x: Optional[np.ndarray] = None) -> pd.Series:
    """
    Fit kernel density estimation to observations.

    Args:
        obs: Observations to fit
        bWidth: Bandwidth parameter
        kernel: Kernel type
        x: Optional evaluation points

    Returns:
        Fitted PDF as pandas Series
    """
    if len(obs.shape) == 1:
        obs = obs.reshape(-1, 1)
    kde = KernelDensity(kernel=kernel, bandwidth=bWidth).fit(obs)
    if x is None:
        x = np.unique(obs).reshape(-1, 1)
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
    logProb = kde.score_samples(x)
    return pd.Series(np.exp(logProb), index=x.flatten())


def getRndCov(nCols: int, nFacts: int) -> np.ndarray:
    """
    Generate random covariance matrix.

    Args:
        nCols: Number of columns
        nFacts: Number of factors

    Returns:
        Random covariance matrix
    """
    w = np.random.normal(size=(nCols, nFacts))
    cov = np.dot(w, w.T)
    cov += np.diag(np.random.uniform(size=nCols))
    return cov


def cov2corr(cov: np.ndarray) -> np.ndarray:
    """
    Convert covariance matrix to correlation matrix.

    Args:
        cov: Covariance matrix

    Returns:
        Correlation matrix
    """
    std = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std, std)
    corr[corr < -1], corr[corr > 1] = -1, 1
    return corr


def corr2cov(corr: np.ndarray, std: np.ndarray) -> np.ndarray:
    """
    Convert correlation matrix to covariance matrix.

    Args:
        corr: Correlation matrix
        std: Standard deviations

    Returns:
        Covariance matrix
    """
    corr[corr < -1], corr[corr > 1] = -1, 1
    return np.outer(std, std) * corr


def errPDFs(var: List[float], eVal: np.ndarray, q: float,
            bWidth: float, pts: int = 1000) -> float:
    """
    Calculate error between theoretical and empirical PDFs.

    Args:
        var: Variance parameter (as list for optimization)
        eVal: Eigenvalues
        q: T/N ratio
        bWidth: Bandwidth for KDE
        pts: Number of points for PDF

    Returns:
        Sum of squared errors
    """
    var = var[0]
    pdf0 = mpPDF(var, q, pts)
    pdf1 = fitKDE(eVal, bWidth, x=pdf0.index.values)
    return np.sum((pdf1 - pdf0) ** 2)


def findMaxEval(eVal: np.ndarray, q: float, bWidth: float) -> Tuple[float, float]:
    """
    Find maximum eigenvalue through optimization.

    Args:
        eVal: Eigenvalues
        q: T/N ratio
        bWidth: Bandwidth for KDE

    Returns:
        Tuple of (maximum eigenvalue, optimal variance)
    """
    out = minimize(lambda *x: errPDFs(*x), 0.5, args=(eVal, q, bWidth),
                   bounds=((1E-5, 1-1E-5),))
    var = out['x'][0] if out['success'] else 1
    eMax = var * (1 + (1./q)**0.5)**2
    return eMax, var


def denoisedCorr(eVal: np.ndarray, eVec: np.ndarray, nFacts: int) -> np.ndarray:
    """
    Denoise correlation matrix using constant residual method.

    Args:
        eVal: Eigenvalues matrix
        eVec: Eigenvectors matrix
        nFacts: Number of factors to preserve

    Returns:
        Denoised correlation matrix
    """
    eVal_ = np.diag(eVal).copy()
    eVal_[nFacts:] = eVal_[nFacts:].sum() / float(eVal_.shape[0] - nFacts)
    eVal_ = np.diag(eVal_)
    corr1 = np.dot(eVec, eVal_).dot(eVec.T)
    return cov2corr(corr1)


def denoisedCorr2(eVal: np.ndarray, eVec: np.ndarray, nFacts: int,
                  alpha: float = 0) -> np.ndarray:
    """
    Denoise correlation matrix using targeted shrinkage.

    Args:
        eVal: Eigenvalues matrix
        eVec: Eigenvectors matrix
        nFacts: Number of factors to preserve
        alpha: Shrinkage parameter

    Returns:
        Denoised correlation matrix
    """
    eValL, eVecL = eVal[:nFacts, :nFacts], eVec[:, :nFacts]
    eValR, eVecR = eVal[nFacts:, nFacts:], eVec[:, nFacts:]
    corr0 = np.dot(eVecL, eValL).dot(eVecL.T)
    corr1 = np.dot(eVecR, eValR).dot(eVecR.T)
    return corr0 + alpha * corr1 + (1 - alpha) * np.diag(np.diag(corr1))


def formBlockMatrix(nBlocks: int, bSize: int, bCorr: float) -> np.ndarray:
    """
    Form block matrix for covariance structure.

    Args:
        nBlocks: Number of blocks
        bSize: Block size
        bCorr: Block correlation

    Returns:
        Block correlation matrix
    """
    block = np.ones((bSize, bSize)) * bCorr
    block[range(bSize), range(bSize)] = 1
    return block_diag(*([block] * nBlocks))


def formTrueMatrix(nBlocks: int, bSize: int, bCorr: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Form true matrix with block structure.

    Args:
        nBlocks: Number of blocks
        bSize: Block size
        bCorr: Block correlation

    Returns:
        Tuple of (means vector, covariance matrix)
    """
    corr0 = formBlockMatrix(nBlocks, bSize, bCorr)
    corr0 = pd.DataFrame(corr0)
    cols = corr0.columns.tolist()
    np.random.shuffle(cols)
    corr0 = corr0[cols].loc[cols].copy(deep=True)
    std0 = np.random.uniform(0.05, 0.2, corr0.shape[0])
    cov0 = corr2cov(corr0, std0)
    mu0 = np.random.normal(std0, std0, cov0.shape[0]).reshape(-1, 1)
    return mu0, cov0


def deNoiseCov(cov0: np.ndarray, q: float, bWidth: float) -> np.ndarray:
    """
    Denoise covariance matrix.

    Args:
        cov0: Original covariance matrix
        q: T/N ratio
        bWidth: Bandwidth for KDE

    Returns:
        Denoised covariance matrix
    """
    corr0 = cov2corr(cov0)
    eVal0, eVec0 = getPCA(corr0)
    eMax0, var0 = findMaxEval(np.diag(eVal0), q, bWidth)
    nFacts0 = eVal0.shape[0] - np.diag(eVal0)[::-1].searchsorted(eMax0)
    corr1 = denoisedCorr(eVal0, eVec0, nFacts0)
    return corr2cov(corr1, np.diag(cov0)**0.5)


def optPort(cov: np.ndarray, mu: Optional[np.ndarray] = None) -> np.ndarray:
    """
    Calculate optimal portfolio weights.

    Args:
        cov: Covariance matrix
        mu: Optional expected returns vector

    Returns:
        Optimal portfolio weights
    """
    inv = np.linalg.inv(cov)
    ones = np.ones(shape=(inv.shape[0], 1))
    mu = ones if mu is None else mu
    w = np.dot(inv, mu)
    return w / np.dot(ones.T, w)


def simCovMu(mu0: np.ndarray, cov0: np.ndarray, nObs: int,
             shrink: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulate covariance matrix and means.

    Args:
        mu0: True means
        cov0: True covariance
        nObs: Number of observations
        shrink: Whether to use shrinkage

    Returns:
        Tuple of (simulated means, simulated covariance)
    """
    x = np.random.multivariate_normal(mu0.flatten(), cov0, size=nObs)
    mu1 = x.mean(axis=0).reshape(-1, 1)
    if shrink:
        cov1 = LedoitWolf().fit(x).covariance_
    else:
        cov1 = np.cov(x, rowvar=0)
    return mu1, cov1
