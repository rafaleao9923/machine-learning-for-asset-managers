# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.neighbors import KernelDensity
import matplotlib.pylab as plt
from scipy.optimize import minimize
from scipy.linalg import block_diag
from sklearn.covariance import LedoitWolf

def mpPDF(var, q, pts):
    eMin, eMax = var * (1 - (1. / q) ** .5) ** 2, var * (1 + (1. / q) ** .5) ** 2
    eVal = np.linspace(eMin, eMax, pts)
    pdf = q / (2 * np.pi * var * eVal) * ((eMax - eVal) * (eVal - eMin)) ** .5
    pdf = pd.Series(pdf, index=eVal)
    return pdf

def getPCA(matrix):
    eVal, eVec = np.linalg.eig(matrix)
    indices = eVal.argsort()[::-1]
    eVal, eVec = eVal[indices], eVec[:, indices]
    eVal = np.diagflat(eVal)
    return eVal, eVec

def fitKDE(obs, bWidth=.15, kernel='gaussian', x=None):
    if len(obs.shape) == 1: obs = obs.reshape(-1, 1)
    kde = KernelDensity(kernel=kernel, bandwidth=bWidth).fit(obs)
    if x is None: x = np.unique(obs).reshape(-1, 1)
    if len(x.shape) == 1: x = x.reshape(-1, 1)
    logProb = kde.score_samples(x)
    pdf = pd.Series(np.exp(logProb), index=x.flatten())
    return pdf

def getRndCov(nCols, nFacts):
    w = np.random.normal(size=(nCols, nFacts))
    cov = np.dot(w, w.T)
    cov += np.diag(np.random.uniform(size=nCols))
    return cov

def cov2corr(cov):
    std = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std, std)
    corr[corr < -1], corr[corr > 1] = -1, 1
    return corr

def corr2cov(corr, std):
    cov = corr * np.outer(std, std)
    return cov

def errPDFs(var, eVal, q, bWidth, pts=1000):
    var = var[0]
    pdf0 = mpPDF(var, q, pts)
    pdf1 = fitKDE(eVal, bWidth, x=pdf0.index.values)
    sse = np.sum((pdf1 - pdf0) ** 2)
    return sse

def findMaxEval(eVal, q, bWidth):
    out = minimize(lambda *x: errPDFs(*x), x0=np.array(0.5), args=(eVal, q, bWidth), bounds=((1E-5, 1 - 1E-5),))
    if out['success']: var = out['x'][0]
    else: var = 1
    eMax = var * (1 + (1. / q) ** .5) ** 2
    return eMax, var

def denoisedCorr(eVal, eVec, nFacts):
    eVal_ = np.diag(eVal).copy()
    eVal_[nFacts:] = eVal_[nFacts:].sum() / float(eVal_.shape[0] - nFacts)
    eVal_ = np.diag(eVal_)
    corr1 = np.dot(eVec, eVal_).dot(eVec.T)
    corr1 = cov2corr(corr1)
    return corr1

def detoned_corr(corr, eigenvalues, eigenvectors, market_component=1):
    eigenvalues_mark = eigenvalues[:market_component, :market_component]
    eigenvectors_mark = eigenvectors[:, :market_component]
    corr_mark = np.dot(eigenvectors_mark, eigenvalues_mark).dot(eigenvectors_mark.T)
    corr = corr - corr_mark
    corr = cov2corr(corr)
    return corr

def test_detone():
    cov_matrix = np.array([[0.01, 0.002, -0.001],
                           [0.002, 0.04, -0.006],
                           [-0.001, -0.006, 0.01]])
    cor_test = np.corrcoef(cov_matrix, rowvar=0)
    eVal_test, eVec_test = getPCA(cor_test)
    eMax_test, var_test = findMaxEval(np.diag(eVal_test), q, bWidth=.01)
    nFacts_test = eVal_test.shape[0] - np.diag(eVal_test)[::-1].searchsorted(eMax_test)
    corr1_test = denoisedCorr(eVal_test, eVec_test, nFacts_test)
    eVal_denoised_test, eVec_denoised_test = getPCA(corr1_test)
    corr_detoned_denoised_test = detoned_corr(corr1_test, eVal_denoised_test, eVec_denoised_test)
    eVal_detoned_denoised_test, _ = getPCA(corr_detoned_denoised_test)

if __name__ == '__main__':
    N = 1000
    T = 10000
    x = np.random.normal(0, 1, size=(T, N))
    cor = np.corrcoef(x, rowvar=0)
    eVal0, eVec0 = getPCA(cor)
    pdf0 = mpPDF(1., q=x.shape[0] / float(x.shape[1]), pts=N)
    pdf1 = fitKDE(np.diag(eVal0), bWidth=.005)

    alpha, nCols, nFact, q = .995, 1000, 100, 10
    pdf0 = mpPDF(1., q=x.shape[0] / float(x.shape[1]), pts=N)
    cov = np.cov(np.random.normal(size=(nCols * q, nCols)), rowvar=0)
    cov = alpha * cov + (1 - alpha) * getRndCov(nCols, nFact)
    corr0 = cov2corr(cov)
    eVal01, eVec01 = getPCA(corr0)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(np.diag(eVal01), density=True, bins=50)

    eMax0, var0 = findMaxEval(np.diag(eVal01), q, bWidth=.01)
    nFacts0 = eVal01.shape[0] - np.diag(eVal01)[::-1].searchsorted(eMax0)
    
    pdf0 = mpPDF(var0, q=x.shape[0] / float(x.shape[1]), pts=N)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(np.diag(eVal01), density=True, bins=50)

    plt.plot(pdf0.keys(), pdf0, color='r', label="Marcenko-Pastur pdf")
    plt.legend(loc="upper right")
    plt.show()

    corr1 = denoisedCorr(eVal01, eVec01, nFacts0)
    eVal1, eVec1 = getPCA(corr1)

    denoised_eigenvalue = np.diag(eVal1)
    eigenvalue_prior = np.diag(eVal01)
    plt.plot(range(0, len(denoised_eigenvalue)), np.log(denoised_eigenvalue), color='r', label="Denoised eigen-function")
    plt.plot(range(0, len(eigenvalue_prior)), np.log(eigenvalue_prior), color='g', label="Original eigen-function")
    plt.xlabel("Eigenvalue number")
    plt.ylabel("Eigenvalue (log-scale)")
    plt.legend(loc="upper right")
    plt.show()

    corr_detoned_denoised = detoned_corr(corr1, eVal1, eVec1)
    eVal1_detoned, eVec1_detoned = getPCA(corr_detoned_denoised)
    detoned_denoised_eigenvalue = np.diag(eVal1_detoned)
    denoised_eigenvalue = np.diag(eVal1)
    eigenvalue_prior = np.diag(eVal01)

    plt.plot(range(0, len(detoned_denoised_eigenvalue)), np.log(detoned_denoised_eigenvalue), color='b', label="Detoned, denoised eigen-function")
    plt.plot(range(0, len(denoised_eigenvalue)), np.log(denoised_eigenvalue), color='r', label="Denoised eigen-function")
    plt.plot(range(0, len(eigenvalue_prior)), np.log(eigenvalue_prior), color='g', label="Original eigen-function")
    plt.xlabel("Eigenvalue number")
    plt.ylabel("Eigenvalue (log-scale)")
    plt.legend(loc="upper right")
    plt.show()