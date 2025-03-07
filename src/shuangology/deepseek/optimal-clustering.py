import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples
from scipy.linalg import block_diag
from sklearn.utils import check_random_state
import seaborn as sns

def cluster_kmeans_base(corr, max_num_clusters=10, n_init=10):
    """
    Perform base clustering using KMeans on a correlation matrix.
    
    Parameters:
    - corr: Correlation matrix (pd.DataFrame).
    - max_num_clusters: Maximum number of clusters to consider.
    - n_init: Number of initializations for KMeans.
    
    Returns:
    - corr1: Reordered correlation matrix.
    - clusters: Dictionary of clusters.
    - silh: Silhouette scores.
    """
    x = ((1 - corr.fillna(0)) / 2.) ** 0.5  # Observations matrix
    silh = pd.Series()
    
    for init in range(n_init):
        for i in range(2, max_num_clusters + 1):
            kmeans = KMeans(n_clusters=i, n_init=1, n_jobs=1)
            kmeans.fit(x)
            silh_ = silhouette_samples(x, kmeans.labels_)
            stat = (silh_.mean() / silh_.std(), silh.mean() / silh.std())
            if np.isnan(stat[1]) or stat[0] > stat[1]:
                silh, kmeans = silh_, kmeans
    
    new_idx = np.argsort(kmeans.labels_)
    corr1 = corr.iloc[new_idx, new_idx]  # Reorder rows and columns
    clusters = {i: corr.columns[np.where(kmeans.labels_ == i)[0]].tolist() for i in np.unique(kmeans.labels_)}
    silh = pd.Series(silh, index=x.index)
    
    return corr1, clusters, silh

def cluster_kmeans_top(corr, max_num_clusters=None, n_init=3):
    """
    Perform top-level clustering using KMeans on a correlation matrix.
    
    Parameters:
    - corr: Correlation matrix (pd.DataFrame).
    - max_num_clusters: Maximum number of clusters to consider.
    - n_init: Number of initializations for KMeans.
    
    Returns:
    - corr1: Reordered correlation matrix.
    - clusters: Dictionary of clusters.
    - silh: Silhouette scores.
    """
    if max_num_clusters is None:
        max_num_clusters = corr.shape[1] - 1
    
    corr1, clusters, silh = cluster_kmeans_base(corr, max_num_clusters=max_num_clusters, n_init=n_init)
    cluster_tstats = {i: np.mean(silh[clusters[i]]) / np.std(silh[clusters[i]]) for i in clusters.keys()}
    tstat_mean = np.mean(list(cluster_tstats.values()))
    
    redo_clusters = [i for i in cluster_tstats.keys() if cluster_tstats[i] < tstat_mean]
    if len(redo_clusters) <= 1:
        return corr1, clusters, silh
    
    keys_redo = [j for i in redo_clusters for j in clusters[i]]
    corr_tmp = corr.loc[keys_redo, keys_redo]
    corr2, clusters2, silh2 = cluster_kmeans_top(corr_tmp, max_num_clusters=max_num_clusters, n_init=n_init)
    
    corr_new, clusters_new, silh_new = make_new_outputs(corr, {i: clusters[i] for i in clusters.keys() if i not in redo_clusters}, clusters2)
    new_tstat_mean = np.mean([np.mean(silh_new[clusters_new[i]]) / np.std(silh_new[clusters_new[i]]) for i in clusters_new.keys()])
    
    if new_tstat_mean <= tstat_mean:
        return corr1, clusters, silh
    else:
        return corr_new, clusters_new, silh_new

def make_new_outputs(corr, clusters, clusters2):
    """
    Combine clusters and create new outputs.
    
    Parameters:
    - corr: Original correlation matrix.
    - clusters: Original clusters.
    - clusters2: New clusters.
    
    Returns:
    - corr_new: New reordered correlation matrix.
    - clusters_new: Combined clusters.
    - silh_new: New silhouette scores.
    """
    clusters_new = {}
    for i in clusters.keys():
        clusters_new[len(clusters_new.keys())] = list(clusters[i])
    for i in clusters2.keys():
        clusters_new[len(clusters_new.keys())] = list(clusters2[i])
    
    new_idx = [j for i in clusters_new for j in clusters_new[i]]
    corr_new = corr.loc[new_idx, new_idx]
    
    x = ((1 - corr.fillna(0)) / 2.) ** 0.5
    kmeans_labels = np.zeros(len(x.columns))
    for i in clusters_new.keys():
        idxs = [x.index.get_loc(k) for k in clusters_new[i]]
        kmeans_labels[idxs] = i
    
    silh_new = pd.Series(silhouette_samples(x, kmeans_labels), index=x.index)
    return corr_new, clusters_new, silh_new

def random_block_corr(n_cols, n_blocks, min_block_size=1, random_state=None):
    """
    Generate a random block correlation matrix.
    
    Parameters:
    - n_cols: Number of columns (assets).
    - n_blocks: Number of blocks.
    - min_block_size: Minimum size of each block.
    - random_state: Random seed.
    
    Returns:
    - corr: Random block correlation matrix.
    """
    rng = check_random_state(random_state)
    parts = rng.choice(range(1, n_cols - (min_block_size - 1) * n_blocks), n_blocks - 1, replace=False)
    parts.sort()
    parts = np.append(parts, n_cols - (min_block_size - 1) * n_blocks)
    parts = np.append(parts[0], np.diff(parts)) - 1 + min_block_size
    
    cov = None
    for n_cols_ in parts:
        cov_ = get_cov_sub(int(max(n_cols_ * (n_cols_ + 1) / 2., 100)), n_cols_, sigma=0.5, random_state=rng)
        if cov is None:
            cov = cov_.copy()
        else:
            cov = block_diag(cov, cov_)
    
    cov1 = get_cov_sub(n_cols, n_cols, sigma=1.0, random_state=rng)  # Add noise
    cov += cov1
    corr = cov2corr(cov)
    return pd.DataFrame(corr)

def get_cov_sub(n_obs, n_cols, sigma, random_state=None):
    """
    Generate a sub-correlation matrix.
    
    Parameters:
    - n_obs: Number of observations.
    - n_cols: Number of columns.
    - sigma: Standard deviation of noise.
    - random_state: Random seed.
    
    Returns:
    - cov: Sub-correlation matrix.
    """
    rng = check_random_state(random_state)
    ar0 = rng.normal(size=(n_obs, 1))
    ar0 = np.repeat(ar0, n_cols, axis=1)
    ar0 += rng.normal(scale=sigma, size=ar0.shape)
    return np.cov(ar0, rowvar=False)

def cov2corr(cov):
    """
    Convert covariance matrix to correlation matrix.
    
    Parameters:
    - cov: Covariance matrix.
    
    Returns:
    - corr: Correlation matrix.
    """
    std = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std, std)
    corr[corr < -1], corr[corr > 1] = -1, 1  # Numerical error correction
    return corr