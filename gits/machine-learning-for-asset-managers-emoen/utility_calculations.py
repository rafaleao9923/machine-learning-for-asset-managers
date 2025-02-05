# -*- coding: utf-8 -*-
import yfinance as yf
import numpy as np
import pandas as pd
# https://pypi.org/project/onc/

def calculate_correlation(S, T=936, N=234):
    M = np.sum(S, axis=1) / T
    de_meaned_S = S - M[:, None]
    covariance = (np.dot(de_meaned_S, de_meaned_S.T)) / (N - 1)
    corr = correlation_from_covariance(covariance)
    eigenvalue, eigenvector = np.linalg.eig(np.corrcoef(S))
    eigenvalue = abs(eigenvalue)
    condition_num = max(eigenvalue) - min(eigenvalue)

def correlation_from_covariance(covariance):
    v = np.sqrt(np.diag(covariance))
    outer_v = np.outer(v, v)
    correlation = covariance / outer_v
    correlation[covariance == 0] = 0
    return correlation

if __name__ == '__main__':
    N = 234 
    T = 936
    stockPrice = np.loadtxt('csv/ol184.csv', delimiter=',')
    ol = pd.read_csv('csv/ol_ticker.csv', sep='\t', header=None)
    portfolio_name = ol[0]
    stockPrice = stockPrice[:, 1:184]
    returns = pd.DataFrame(stockPrice).pct_change().dropna(how="all")
    calculate_correlation(returns.to_numpy(), T=936, N=234)