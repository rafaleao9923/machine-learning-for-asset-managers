import numpy as np
import pandas as pd
from sklearn.neighbors import KernelDensity
from scipy.optimize import minimize
from sklearn.covariance import LedoitWolf

def mpPDF(var, q, pts=1000):
    eMin, eMax = var * (1 - (1 / q) ** 0.5) ** 2, var * (1 + (1 / q) ** 0.5) ** 2
    eVal = np.linspace(eMin, eMax, pts)
    pdf = q / (2 * np.pi * var * eVal) * ((eMax - eVal) * (eVal - eMin)) ** 0.5
    return pd.Series(pdf, index=eVal)

def getPCA(matrix):
    eVal, eVec = np.linalg.eigh(matrix)
    indices = np.argsort(eVal)[::-1]
    eVal, eVec = eVal[indices], eVec[:, indices]
    return np.diag(eVal), eVec

def fitKDE(obs, bWidth=0.25, kernel='gaussian', x=None):
    obs = obs.reshape(-1, 1) if obs.ndim == 1 else obs
    kde = KernelDensity(kernel=kernel, bandwidth=bWidth).fit(obs)
    x = np.linspace(obs.min(), obs.max(), 1000).reshape(-1, 1) if x is None else x
    logProb = kde.score_samples(x)
    return pd.Series(np.exp(logProb), index=x.flatten())

def findMaxEval(eVal, q, bWidth):
    def errPDFs(var, eVal, q, bWidth):
        pdf_theo = mpPDF(var, q)
        pdf_emp = fitKDE(eVal, bWidth, x=pdf_theo.index)
        return np.sum((pdf_emp - pdf_theo) ** 2)
    result = minimize(errPDFs, 0.5, args=(eVal, q, bWidth), bounds=[(1e-5, 1)])
    var = result.x[0] if result.success else 1
    eMax = var * (1 + (1 / q) ** 0.5) ** 2
    return eMax, var

def denoisedCorr(eVal, eVec, nFacts):
    eVal = np.diag(eVal)
    eVal[nFacts:] = eVal[nFacts:].mean()
    corr1 = eVec @ np.diag(eVal) @ eVec.T
    return cov2corr(corr1)

def deNoiseCov(cov, q, bWidth):
    corr0 = cov2corr(cov)
    eVal, eVec = getPCA(corr0)
    eMax, _ = findMaxEval(np.diag(eVal), q, bWidth)
    nFacts = np.sum(np.diag(eVal) > eMax)
    corr1 = denoisedCorr(eVal, eVec, nFacts)
    return corr2cov(corr1, np.sqrt(np.diag(cov)))

def cov2corr(cov):
    std_dev = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std_dev, std_dev)
    np.clip(corr, -1, 1, out=corr)
    return corr

def corr2cov(corr, std):
    return np.outer(std, std) * corr

def optPort(cov, mu=None):
    inv = np.linalg.inv(cov)
    ones = np.ones((inv.shape[0], 1))
    mu = ones if mu is None else mu.reshape(-1, 1)
    w = inv @ mu
    return (w / (ones.T @ w)).flatten()
