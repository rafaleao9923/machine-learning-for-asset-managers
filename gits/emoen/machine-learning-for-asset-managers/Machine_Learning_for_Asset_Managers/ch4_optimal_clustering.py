import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.utils import check_random_state
from scipy.linalg import block_diag
import matplotlib.pylab as plt

from Machine_Learning_for_Asset_Managers import ch2_marcenko_pastur_pdf as mp

def clusterKMeansBase(corr0, maxNumClusters=10, n_init=10, debug=False):
    corr0[corr0 > 1] = 1
    dist_matrix = ((1 - corr0.fillna(0)) / 2.) ** .5
    silh_coef_optimal = pd.Series(dtype='float64')
    kmeans = None
    maxNumClusters = min(maxNumClusters, int(np.floor(dist_matrix.shape[0] / 2)))
    for init in range(n_init):
        for num_clusters in range(2, maxNumClusters + 1):
            kmeans_ = KMeans(n_clusters=num_clusters, n_init=10)
            kmeans_ = kmeans_.fit(dist_matrix)
            silh_coef = silhouette_samples(dist_matrix, kmeans_.labels_)
            stat = (silh_coef.mean() / silh_coef.std(), silh_coef_optimal.mean() / silh_coef_optimal.std())
            if np.isnan(stat[1]) or stat[0] > stat[1]:
                silh_coef_optimal = silh_coef
                kmeans = kmeans_
                if debug:
                    silhouette_avg = silhouette_score(dist_matrix, kmeans_.labels_)
                    print("For n_clusters =" + str(num_clusters) + " The average silhouette_score is :" + str(silhouette_avg))
    
    newIdx = np.argsort(kmeans.labels_)
    corr1 = corr0.iloc[newIdx]
    corr1 = corr1.iloc[:, newIdx]
    clstrs = {i: corr0.columns[np.where(kmeans.labels_ == i)[0]].tolist() for i in np.unique(kmeans.labels_)}
    silh_coef_optimal = pd.Series(silh_coef_optimal, index=dist_matrix.index)
    
    return corr1, clstrs, silh_coef_optimal

def makeNewOutputs(corr0, clstrs, clstrs2):
    clstrsNew, newIdx = {}, []
    for i in clstrs.keys():
        clstrsNew[len(clstrsNew.keys())] = list(clstrs[i])
    
    for i in clstrs2.keys():
        clstrsNew[len(clstrsNew.keys())] = list(clstrs2[i])
    
    newIdx = [j for i in clstrsNew for j in clstrsNew[i]]
    corrNew = corr0.loc[newIdx, newIdx]
    
    dist = ((1 - corr0.fillna(0)) / 2.) ** .5
    kmeans_labels = np.zeros(len(dist.columns))
    for i in clstrsNew.keys():
        idxs = [dist.index.get_loc(k) for k in clstrsNew[i]]
        kmeans_labels[idxs] = i
    
    silhNew = pd.Series(silhouette_samples(dist, kmeans_labels), index=dist.index)
    
    return corrNew, clstrsNew, silhNew

def clusterKMeansTop(corr0: pd.DataFrame, maxNumClusters=None, n_init=10):
    if maxNumClusters is None:
        maxNumClusters = corr0.shape[1] - 1
        
    corr1, clstrs, silh = clusterKMeansBase(corr0, maxNumClusters=min(maxNumClusters, corr0.shape[1] - 1), n_init=n_init)
    clusterTstats = {i: np.mean(silh[clstrs[i]]) / np.std(silh[clstrs[i]]) for i in clstrs.keys()}
    tStatMean = sum(clusterTstats.values()) / len(clusterTstats)
    redoClusters = [i for i in clusterTstats.keys() if clusterTstats[i] < tStatMean]
    
    if len(redoClusters) <= 2:
        return corr1, clstrs, silh
    else:
        keysRedo = [j for i in redoClusters for j in clstrs[i]]
        corrTmp = corr0.loc[keysRedo, keysRedo]
        _, clstrs2, _ = clusterKMeansTop(corrTmp, maxNumClusters=min(maxNumClusters, corrTmp.shape[1] - 1), n_init=n_init)
        dict_redo_clstrs = {i: clstrs[i] for i in clstrs.keys() if i not in redoClusters}
        corrNew, clstrsNew, silhNew = makeNewOutputs(corr0, dict_redo_clstrs, clstrs2)
        newTstatMean = np.mean([np.mean(silhNew[clstrsNew[i]]) / np.std(silhNew[clstrsNew[i]]) for i in clstrsNew.keys()])
        
        if newTstatMean <= tStatMean:
            return corr1, clstrs, silh
        else:
            return corrNew, clstrsNew, silhNew

def getCovSub(nObs, nCols, sigma, random_state=None):
    rng = check_random_state(random_state)
    if nCols == 1:
        return np.ones((1, 1))
    ar0 = rng.normal(size=(nObs, 1))
    ar0 = np.repeat(ar0, nCols, axis=1)
    ar0 += rng.normal(loc=0, scale=sigma, size=ar0.shape)
    ar0 = np.cov(ar0, rowvar=False)
    return ar0

def getRndBlockCov(nCols, nBlocks, minBlockSize=1, sigma=1., random_state=None):
    rng = check_random_state(random_state)
    parts = rng.choice(range(1, nCols - (minBlockSize - 1) * nBlocks), nBlocks - 1, replace=False)
    parts.sort()
    parts = np.append(parts, nCols - (minBlockSize - 1) * nBlocks)
    parts = np.append(parts[0], np.diff(parts)) - 1 + minBlockSize
    cov = None
    for nCols_ in parts:
        cov_ = getCovSub(int(max(nCols_ * (nCols_ + 1) / 2., 100)), nCols_, sigma, random_state=rng)
        if cov is None:
            cov = cov_.copy()
        else:
            cov = block_diag(cov, cov_)
    
    return cov

def randomBlockCorr(nCols, nBlocks, random_state=None, minBlockSize=1):
    rng = check_random_state(random_state)
    cov0 = getRndBlockCov(nCols, nBlocks, minBlockSize=minBlockSize, sigma=.5, random_state=rng)
    cov1 = getRndBlockCov(nCols, 1, minBlockSize=minBlockSize, sigma=1., random_state=rng)
    cov0 += cov1
    corr0 = mp.cov2corr(cov0)
    corr0 = pd.DataFrame(corr0)
    return corr0

if __name__ == '__main__':
    nCols, nBlocks = 6, 3
    nObs = 8
    sigma = 1.
    corr0 = randomBlockCorr(nCols, nBlocks)
    testGetCovSub = getCovSub(nObs, nCols, sigma, random_state=None)
    
    nCols, nBlocks, minBlockSize = 30, 6, 2
    corr0 = randomBlockCorr(nCols, nBlocks, minBlockSize=minBlockSize)
    corr1 = clusterKMeansTop(corr0)

    plt.matshow(corr0)
    plt.gca().xaxis.tick_bottom()
    plt.gca().invert_yaxis()
    plt.colorbar()
    plt.show()

    corrNew, clstrsNew, silhNew = clusterKMeansTop(corr0)
    plt.matshow(corrNew)
    plt.gca().xaxis.tick_bottom()
    plt.gca().invert_yaxis()
    plt.colorbar()
    plt.show()