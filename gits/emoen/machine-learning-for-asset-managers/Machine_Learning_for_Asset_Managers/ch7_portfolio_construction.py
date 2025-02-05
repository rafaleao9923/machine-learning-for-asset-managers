# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from scipy.linalg import block_diag
import matplotlib.pylab as plt
import seaborn as sns

from Machine_Learning_for_Asset_Managers import ch2_monte_carlo_experiment as mc
from Machine_Learning_for_Asset_Managers import ch2_marcenko_pastur_pdf as mp
from Machine_Learning_for_Asset_Managers import ch4_optimal_clustering as oc

def minVarPort(cov):
    return mc.optPort(cov, mu=None)

def optPort_nco(cov, mu=None, maxNumClusters=None):
    cov = pd.DataFrame(cov)
    if mu is not None:
        mu = pd.Series(mu[:, 0])
    
    corr1 = mp.cov2corr(cov)
    corr1, clstrs, _ = oc.clusterKMeansBase(corr1, maxNumClusters, n_init=10)
    w_intra_clusters = pd.DataFrame(0, index=cov.index, columns=clstrs.keys())
    for i in clstrs:
        cov_cluster = cov.loc[clstrs[i], clstrs[i]].values
        mu_cluster = mu.loc[clstrs[i]].values.reshape(-1, 1) if mu is not None else None
        w_intra_clusters.loc[clstrs[i], i] = allocate_cvo(cov_cluster, mu_cluster).flatten()

    cov_inter_cluster = w_intra_clusters.T.dot(np.dot(cov, w_intra_clusters))
    mu_inter_cluster = (None if mu is None else w_intra_clusters.T.dot(mu))
    w_inter_clusters = pd.Series(allocate_cvo(cov_inter_cluster, mu_inter_cluster).flatten(), index=cov_inter_cluster.index)
    nco = w_intra_clusters.mul(w_inter_clusters, axis=1).sum(axis=1).values.reshape(-1, 1)
    return nco

def allocate_cvo(cov, mu_vec=None):
    inv_cov = np.linalg.inv(cov)
    ones = np.ones(shape=(inv_cov.shape[0], 1))
    
    if mu_vec is None:
        mu_vec = ones
    
    w_cvo = np.dot(inv_cov, mu_vec)
    w_cvo /= np.dot(mu_vec.T, w_cvo)
    
    return w_cvo

if __name__ == '__main__':
    corr0 = mc.formBlockMatrix(2, 2, .5)
    eVal, eVec = np.linalg.eigh(corr0)
    matrix_condition_number = max(eVal) / min(eVal)
    print(matrix_condition_number)

    fig, ax = plt.subplots(figsize=(13, 10))
    sns.heatmap(corr0, cmap='viridis')
    plt.show()

    corr0 = block_diag(mc.formBlockMatrix(1, 2, .5))
    corr1 = mc.formBlockMatrix(1, 2, .0)
    corr0 = block_diag(corr0, corr1)
    eVal, eVec = np.linalg.eigh(corr0)
    matrix_condition_number = max(eVal) / min(eVal)
    print(matrix_condition_number)

    fig, ax = plt.subplots(figsize=(13, 10))
    sns.heatmap(corr1, cmap='viridis')
    plt.show()

    nBlocks, bSize, bCorr = 2, 2, .5
    q = 10.0
    np.random.seed(0)
    mu0, cov0 = mc.formTrueMatrix(nBlocks, bSize, bCorr)
    cols = cov0.columns
    cov1 = mc.deNoiseCov(cov0, q, bWidth=.01)
    cov1 = pd.DataFrame(cov1, index=cols, columns=cols)
    corr1 = mp.cov2corr(cov1)
    corr1, clstrs, silh = oc.clusterKMeansBase(pd.DataFrame(corr0))

    wIntra = pd.DataFrame(0, index=cov0.index, columns=clstrs.keys())
    for i in clstrs:
        wIntra.loc[clstrs[i], i] = minVarPort(cov1.loc[clstrs[i], clstrs[i]]).flatten()
        
    cov2 = wIntra.T.dot(np.dot(cov1, wIntra))

    wInter = pd.Series(minVarPort(cov2).flatten(), index=cov2.index)
    wAll0 = wIntra.mul(wInter, axis=1).sum(axis=1).sort_index()

    nBlocks, bSize, bCorr = 10, 50, .5
    np.random.seed(0)
    mu0, cov0 = mc.formTrueMatrix(nBlocks, bSize, bCorr)
       
    nObs, nSims, shrink, minVarPortf = 1000, 1000, False, True
    np.random.seed(0)
    w1 = pd.DataFrame(0, index=range(0, nSims), columns=range(0, nBlocks * bSize))
    w1_d = pd.DataFrame(0, index=range(0, nSims), columns=range(0, nBlocks * bSize))
    for i in range(0, nSims):
        mu1, cov1 = mc.simCovMu(mu0, cov0, nObs, shrink=shrink)
        if minVarPortf:
            mu1 = None
        w1.loc[i] = mc.optPort(cov1, mu1).flatten()
        w1_d.loc[i] = optPort_nco(cov1, mu1, int(cov1.shape[0] / 2)).flatten()

    w0 = mc.optPort(cov0, None if minVarPortf else mu0)
    w0 = np.repeat(w0.T, w1.shape[0], axis=0)
    rmsd = np.mean((w1 - w0).values.flatten() ** 2) ** .5
    rmsd_d = np.mean((w1_d - w0).values.flatten() ** 2) ** .5