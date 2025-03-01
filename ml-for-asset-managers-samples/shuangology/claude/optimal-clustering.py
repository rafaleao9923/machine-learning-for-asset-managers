"""
Optimal Clustering Implementation.

This module implements various clustering algorithms for financial correlation matrices,
including hierarchical clustering, K-means, and random block generation utilities.
"""

from typing import Dict, Tuple, List, Optional, Union
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples
from sklearn.utils import check_random_state
from scipy.linalg import block_diag

def clusterKMeansBase(corr0: pd.DataFrame, 
                      maxNumClusters: int = 10,
                      n_init: int = 10) -> Tuple[pd.DataFrame, Dict, pd.Series]:
    """
    Perform base K-means clustering on correlation matrix.
    
    Args:
        corr0: Correlation matrix
        maxNumClusters: Maximum number of clusters to try
        n_init: Number of initialization attempts
        
    Returns:
        Tuple of (reordered correlation matrix, cluster assignments, silhouette scores)
    """
    # Transform correlations to distances
    x = ((1 - corr0.fillna(0)) / 2.)**0.5
    best_silh = pd.Series()
    best_kmeans = None
    
    for init in range(n_init):
        for n_clusters in range(2, maxNumClusters + 1):
            kmeans = KMeans(n_clusters=n_clusters, n_init=1)
            kmeans.fit(x)
            silh = silhouette_samples(x, kmeans.labels_)
            
            # Compare clustering quality
            stat = (silh.mean() / silh.std())
            if not best_silh.size or stat > (best_silh.mean() / best_silh.std()):
                best_silh = pd.Series(silh, index=x.index)
                best_kmeans = kmeans

    # Reorder correlation matrix
    idx = np.argsort(best_kmeans.labels_)
    corr1 = corr0.iloc[idx].iloc[:, idx]
    
    # Create cluster assignments
    clusters = {i: corr0.columns[np.where(best_kmeans.labels_ == i)[0]].tolist()
               for i in np.unique(best_kmeans.labels_)}
    
    return corr1, clusters, best_silh

def makeNewOutputs(corr0: pd.DataFrame,
                   clstrs: Dict,
                   clstrs2: Dict) -> Tuple[pd.DataFrame, Dict, pd.Series]:
    """
    Combine results from multiple clustering operations.
    
    Args:
        corr0: Original correlation matrix
        clstrs: First set of clusters
        clstrs2: Second set of clusters
        
    Returns:
        Tuple of (new correlation matrix, combined clusters, new silhouette scores)
    """
    # Combine clusters
    combined_clusters = {}
    for i, cluster in clstrs.items():
        combined_clusters[len(combined_clusters)] = list(cluster)
    for i, cluster in clstrs2.items():
        combined_clusters[len(combined_clusters)] = list(cluster)
    
    # Reorder correlation matrix
    new_idx = [j for i in combined_clusters.values() for j in i]
    corr_new = corr0.loc[new_idx, new_idx]
    
    # Calculate silhouette scores
    x = ((1 - corr0.fillna(0)) / 2.)**0.5
    labels = np.zeros(len(x.columns))
    for i, members in combined_clusters.items():
        idxs = [x.index.get_loc(k) for k in members]
        labels[idxs] = i
        
    silh_new = pd.Series(silhouette_samples(x, labels), index=x.index)
    return corr_new, combined_clusters, silh_new

def clusterKMeansTop(corr0: pd.DataFrame,
                     maxNumClusters: Optional[int] = None,
                     n_init: int = 3) -> Tuple[pd.DataFrame, Dict, pd.Series]:
    """
    Perform recursive optimal clustering.
    
    Args:
        corr0: Correlation matrix
        maxNumClusters: Maximum number of clusters
        n_init: Number of initialization attempts
        
    Returns:
        Tuple of (clustered correlation matrix, cluster assignments, silhouette scores)
    """
    if maxNumClusters is None:
        maxNumClusters = corr0.shape[1] - 1
        
    # Initial clustering
    corr1, clusters, silh = clusterKMeansBase(
        corr0,
        maxNumClusters=min(maxNumClusters, corr0.shape[1] - 1),
        n_init=n_init
    )
    
    # Calculate cluster quality
    cluster_stats = {
        i: np.mean(silh[clusters[i]]) / np.std(silh[clusters[i]])
        for i in clusters
    }
    mean_stat = np.mean(list(cluster_stats.values()))
    
    # Find clusters to redo
    redo_clusters = [i for i, stat in cluster_stats.items() if stat < mean_stat]
    
    if len(redo_clusters) <= 1:
        return corr1, clusters, silh
        
    # Recluster poor quality clusters
    redo_keys = [j for i in redo_clusters for j in clusters[i]]
    corr_tmp = corr0.loc[redo_keys, redo_keys]
    
    corr2, clusters2, silh2 = clusterKMeansTop(
        corr_tmp,
        maxNumClusters=min(maxNumClusters, corr_tmp.shape[1] - 1),
        n_init=n_init
    )
    
    # Combine results
    keep_clusters = {i: clusters[i] for i in clusters if i not in redo_clusters}
    corr_new, clusters_new, silh_new = makeNewOutputs(
        corr0, keep_clusters, clusters2
    )
    
    # Compare quality
    new_stats = [
        np.mean(silh_new[clusters_new[i]]) / np.std(silh_new[clusters_new[i]])
        for i in clusters_new
    ]
    
    if np.mean(new_stats) <= mean_stat:
        return corr1, clusters, silh
    return corr_new, clusters_new, silh_new

def getCovSub(nObs: int,
              nCols: int,
              sigma: float,
              random_state: Optional[int] = None) -> np.ndarray:
    """
    Generate random submatrix for block correlation matrix.
    
    Args:
        nObs: Number of observations
        nCols: Number of columns
        sigma: Standard deviation of noise
        random_state: Random seed
        
    Returns:
        Covariance submatrix
    """
    rng = check_random_state(random_state)
    
    if nCols == 1:
        return np.ones((1, 1))
        
    # Generate correlated data
    base = rng.normal(size=(nObs, 1))
    data = np.repeat(base, nCols, axis=1)
    data += rng.normal(scale=sigma, size=data.shape)
    
    return np.cov(data, rowvar=False)

def getRndBlockCov(nCols: int,
                   nBlocks: int,
                   minBlockSize: int = 1,
                   sigma: float = 1.0,
                   random_state: Optional[int] = None) -> np.ndarray:
    """
    Generate random block covariance matrix.
    
    Args:
        nCols: Total number of columns
        nBlocks: Number of blocks
        minBlockSize: Minimum block size
        sigma: Noise standard deviation
        random_state: Random seed
        
    Returns:
        Block covariance matrix
    """
    rng = check_random_state(random_state)
    
    # Generate random block sizes
    available_space = nCols - (minBlockSize - 1) * nBlocks
    split_points = rng.choice(range(1, available_space), nBlocks - 1, replace=False)
    split_points.sort()
    split_points = np.append(split_points, available_space)
    
    # Calculate block sizes
    block_sizes = np.append(split_points[0], np.diff(split_points)) - 1 + minBlockSize
    
    # Generate blocks
    cov_blocks = []
    for size in block_sizes:
        n_obs = int(max(size * (size + 1) / 2, 100))
        cov_block = getCovSub(n_obs, size, sigma, random_state=rng)
        cov_blocks.append(cov_block)
        
    return block_diag(*cov_blocks)

def randomBlockCorr(nCols: int,
                    nBlocks: int,
                    minBlockSize: int = 1,
                    random_state: Optional[int] = None) -> pd.DataFrame:
    """
    Generate random block correlation matrix.
    
    Args:
        nCols: Number of columns
        nBlocks: Number of blocks
        minBlockSize: Minimum block size
        random_state: Random seed
        
    Returns:
        Random block correlation matrix
    """
    rng = check_random_state(random_state)
    
    # Generate base structure
    cov_structure = getRndBlockCov(
        nCols, nBlocks,
        minBlockSize=minBlockSize,
        sigma=0.5,
        random_state=rng
    )
    
    # Add noise
    cov_noise = getRndBlockCov(
        nCols, 1,
        minBlockSize=minBlockSize,
        sigma=1.0,
        random_state=rng
    )
    
    cov_total = cov_structure + cov_noise
    
    # Convert to correlation matrix
    std = np.sqrt(np.diag(cov_total))
    corr = cov_total / np.outer(std, std)
    corr = pd.DataFrame(corr)
    
    return corr