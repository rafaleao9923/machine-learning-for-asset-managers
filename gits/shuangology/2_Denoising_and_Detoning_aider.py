# 2_Denoising_and_Detoning.py
# Implementation of code snippets and exercises from Chapter 2 of "Machine Learning for Asset Managers"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
from sklearn.neighbors.kde import KernelDensity
from scipy.optimize import minimize
from sklearn.covariance import LedoitWolf
from scipy.linalg import block_diag
import bs4 as bs
import requests
import yfinance as yf
import datetime
import scipy.optimize as opt


def mpPDF(var, q, pts):
    eMin, eMax = var * (1 - (1. / q) ** .5) ** 2, var * \
        (1 + (1. / q) ** .5) ** 2
    eVal = np.linspace(eMin, eMax, pts)
    pdf = q / (2 * np.pi * var * eVal) * ((eMax - eVal) * (eVal - eMin)) ** .5
    pdf = pd.Series(pdf, index=eVal)
    return pdf


def getPCA(matrix):
    eVal, eVec = np.linalg.eigh(matrix)
    indices = eVal.argsort()[::-1]
    eVal, eVec = eVal[indices], eVec[:, indices]
    eVal = np.diagflat(eVal)
    return eVal, eVec


def fitKDE(obs, bWidth=.25, kernel='gaussian', x=None):
    if len(obs.shape) == 1:
        obs = obs.reshape(-1, 1)
    kde = KernelDensity(kernel=kernel, bandwidth=bWidth).fit(obs)
    if x is None:
        x = np.unique(obs).reshape(-1, 1)
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
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


def errPDFs(var, eVal, q, bWidth, pts=1000):
    var = var[0]
    pdf0 = mpPDF(var, q, pts)
    pdf1 = fitKDE(eVal, bWidth, x=pdf0.index.values)
    sse = np.sum((pdf1 - pdf0) ** 2)
    return sse


def findMaxEval(eVal, q, bWidth):
    out = minimize(lambda *x: errPDFs(*x), .5, args=(eVal,
                   q, bWidth), bounds=((1E-5, 1 - 1E-5),))
    if out['success']:
        var = out['x'][0]
    else:
        var = 1
    eMax = var * (1 + (1. / q) ** .5) ** 2
    return eMax, var


def denoisedCorr(eVal, eVec, nFacts):
    eVal_ = np.diag(eVal).copy()
    eVal_[nFacts:] = eVal_[nFacts:].sum() / float(eVal_.shape[0] - nFacts)
    eVal_ = np.diag(eVal_)
    corr1 = np.dot(eVec, eVal_).dot(eVec.T)
    corr1 = cov2corr(corr1)
    return corr1


def denoisedCorr2(eVal, eVec, nFacts, alpha=0):
    eValL, eVecL = eVal[:nFacts, :nFacts], eVec[:, :nFacts]
    eValR, eVecR = eVal[nFacts:, nFacts:], eVec[:, nFacts:]
    corr0 = np.dot(eVecL, eValL).dot(eVecL.T)
    corr1 = np.dot(eVecR, eValR).dot(eVecR.T)
    corr2 = corr0 + alpha * corr1 + (1 - alpha) * np.diag(np.diag(corr1))
    return corr2


def corr2cov(corr, std):
    corr[corr < -1], corr[corr > 1] = -1, 1
    cov = np.outer(std, std) * corr
    return cov


def formBlockMatrix(nBlocks, bSize, bCorr):
    block = np.ones((bSize, bSize)) * bCorr
    block[range(bSize), range(bSize)] = 1
    corr = block_diag(*([block] * nBlocks))
    return corr


def formTrueMatrix(nBlocks, bSize, bCorr):
    corr0 = formBlockMatrix(nBlocks, bSize, bCorr)
    corr0 = pd.DataFrame(corr0)
    cols = corr0.columns.tolist()
    np.random.shuffle(cols)
    corr0 = corr0[cols].loc[cols].copy(deep=True)
    std0 = np.random.uniform(.05, .2, corr0.shape[0])
    cov0 = corr2cov(corr0, std0)
    mu0 = np.random.normal(std0, std0, cov0.shape[0]).reshape(-1, 1)
    return mu0, cov0


def simCovMu(mu0, cov0, nObs, shrink=False):
    x = np.random.multivariate_normal(mu0.flatten(), cov0, size=nObs)
    mu1 = x.mean(axis=0).reshape(-1, 1)
    if shrink:
        cov1 = LedoitWolf().fit(x).covariance_
    else:
        cov1 = np.cov(x, rowvar=0)
    return mu1, cov1


def deNoiseCov(cov0, q, bWidth):
    corr0 = cov2corr(cov0)
    eVal0, eVec0 = getPCA(corr0)
    eMax0, var0 = findMaxEval(np.diag(eVal0), q, bWidth)
    nFacts0 = eVal0.shape[0] - np.diag(eVal0)[::-1].searchsorted(eMax0)
    corr1 = denoisedCorr(eVal0, eVec0, nFacts0)
    cov1 = corr2cov(corr1, np.diag(cov0) ** .5)
    return cov1


def optPort(cov, mu=None):
    inv = np.linalg.inv(cov)
    ones = np.ones(shape=(inv.shape[0], 1))
    if mu is None:
        mu = ones
    w = np.dot(inv, mu)
    w /= np.dot(ones.T, w)
    return w


def portfolio_volatility(weights, day_returns, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))


def portfolio_annualised_performance(weights, day_returns, cov_matrix):
    returns = np.sum(day_returns.T.dot(weights)) * 252
    std = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns


def random_portfolios(num_portfolios, day_returns, cov_matrix):
    results = np.zeros((2, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.normal(0.1, 0.1, len(day_returns))
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(
            weights, day_returns, cov_matrix)
        results[0, i] = portfolio_std_dev
        results[1, i] = portfolio_return
    return results, weights_record


def efficient_return(day_returns, cov_matrix, target):
    num_assets = len(day_returns)
    args = (day_returns, cov_matrix)

    def portfolio_return(weights):
        return portfolio_annualised_performance(weights, day_returns, cov_matrix)[1]

    constraints = ({'type': 'eq', 'fun': lambda x: portfolio_return(x) - target},
                   {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(num_assets))
    result = opt.minimize(portfolio_volatility, num_assets * [
                          1. / num_assets, ], args=args, method='SLSQP', bounds=bounds, constraints=constraints)
    return result


def efficient_frontier(day_returns, cov_matrix, returns_range):
    efficients = []
    for ret in tqdm(returns_range, desc='calculating efficient frontier using optimization method:'):
        efficients.append(efficient_return(day_returns, cov_matrix, ret))
    return efficients


def ef_with_random_portfolio_opt(day_returns, cov_matrix, num_portfolios, ax=None, return_plot=True):
    results, weights = random_portfolios(
        num_portfolios, day_returns, cov_matrix)
    target = np.linspace(
        max(np.min(results[1]), 0), np.quantile(results[1], 0.7), 30)
    efficient_portfolios = efficient_frontier(day_returns, cov_matrix, target)
    frontier = [p['fun'] for p in efficient_portfolios]

    if return_plot:
        if not ax:
            fig = plt.figure(figsize=(10, 7))
            ax = fig.add_subplot(111)
        ax.plot(frontier, target, color='black',
                linewidth=2, label='efficient frontier')
        ax.scatter(results[0, :], results[1, :], marker='o', s=10, alpha=0.3)
        ax.set_title(
            'Calculated Portfolio Optimization based on Efficient Frontier')
        ax.set_xlabel('annualised volatility')
        ax.set_ylabel('annualised returns')
        ax.legend()
    return ax, [frontier, target]


def efficient_return_simu(results, target):
    results = pd.DataFrame(results.T).sort_values(by=1)
    closiest_idx = np.argmin(np.abs(results[1] - target))
    data_target = results[1][closiest_idx]
    target_range_min = min(data_target * 0.95, data_target * 1.05)
    target_range_max = max(data_target * 0.95, data_target * 1.05)
    sub_results = results.loc[(results[1] <= target_range_max) & (
        results[1] >= target_range_min), 0:2]
    return min(sub_results[0])


def efficient_frontier_emp(day_returns, cov_matrix, num_portfolios, returns_range, random_seed=0):
    efficients = []
    np.random.seed(random_seed)
    results, weights = random_portfolios(
        num_portfolios, day_returns, cov_matrix)
    for ret in returns_range:
        efficients.append(efficient_return_simu(results, ret))
    return efficients


def ef_with_random_portfolio_simu(day_returns, cov_matrix, num_portfolios, ax=None, return_plot=True, random_seed=0, mean_frontier=None):
    results, weights = random_portfolios(
        num_portfolios, day_returns, cov_matrix)
    target_start = 0
    if True:
        target_end = 400
    else:
        target_end = results[1][results[0] == np.max(results[0])][0]

    target = np.linspace(target_start, target_end, 30)
    efficient_portfolios = efficient_frontier_emp(
        day_returns, cov_matrix, num_portfolios, target, random_seed=random_seed)

    if return_plot:
        if not ax:
            fig = plt.figure(figsize=(10, 7))
            ax = fig.add_subplot(111)
        if mean_frontier:
            ax.plot(mean_frontier[0], mean_frontier[1], color='black',
                    linewidth=2, label='mean efficient frontier')
        else:
            ax.plot(efficient_portfolios, target, color='black',
                    linewidth=2, label='efficient frontier')
        ax.scatter(results[0, :], results[1, :], marker='o', s=10, alpha=0.3)
        ax.set_title(
            'Calculated Portfolio Optimization based on Efficient Frontier')
        ax.set_xlabel('annualised volatility')
        ax.set_ylabel('annualised returns')
        ax.legend()
    else:
        ax = None
    return ax, [efficient_portfolios, target]


def MC_ef_frontier(day_returns, cov_matrix, itertimes=100, random_seed=3):
    np.random.seed(random_seed)
    target_ret = pd.DataFrame(day_returns.T)
    target_cov = cov_matrix
    frontier = []
    for i in tqdm(range(itertimes)):
        ax, frontier_ret = ef_with_random_portfolio_simu(
            target_ret, target_cov, 1000, return_plot=False, random_seed=i)
        frontier.append(frontier_ret[0])
    mean_frontier_vol = np.mean(frontier, axis=0)
    mean_frontier_ret = frontier_ret[1]
    return mean_frontier_vol, mean_frontier_ret


def error_mean_ef_frontier(frontiers, mean_frontier):
    err = []
    for frontier in frontiers:
        err.append(np.std(frontier - mean_frontier))
    return np.var(err)


if __name__ == "__main__":
    nBlocks, bSize, bCorr = 10, 50, .5
    np.random.seed(0)
    mu0, cov0 = formTrueMatrix(nBlocks, bSize, bCorr)
    print("True Matrix formed with mean and covariance.")
