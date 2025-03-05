import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples
from scipy.linalg import block_diag
from sklearn.utils import check_random_state
from typing import Dict, Tuple
from concurrent.futures import ThreadPoolExecutor

def cluster_kmeans_base(corr: pd.DataFrame, max_num_clusters: int = 10, n_init: int = 10) -> Tuple[pd.DataFrame, Dict, pd.Series]:
    """Optimized base clustering using KMeans."""
    x = np.sqrt((1 - corr.fillna(0)) / 2.)
    best_silh = pd.Series()
    best_kmeans = None
    best_stat = float('-inf')
    
    def run_kmeans(i: int) -> Tuple[pd.Series, KMeans, float]:
        kmeans = KMeans(n_clusters=i, n_init=1, random_state=np.random.randint(0, 1000))
        kmeans.fit(x)
        silh = silhouette_samples(x, kmeans.labels_)
        stat = silh.mean() / silh.std() if silh.std() != 0 else float('-inf')
        return silh, kmeans, stat
    
    with ThreadPoolExecutor() as executor:
        for init in range(n_init):
            futures = [executor.submit(run_kmeans, i) for i in range(2, max_num_clusters + 1)]
            for future in futures:
                silh, kmeans, stat = future.result()
                if stat > best_stat:
                    best_silh, best_kmeans, best_stat = silh, kmeans, stat
    
    new_idx = np.argsort(best_kmeans.labels_)
    corr1 = corr.iloc[new_idx, new_idx]
    clusters = {i: corr.columns[best_kmeans.labels_ == i].tolist() 
               for i in range(best_kmeans.n_clusters)}
    
    return corr1, clusters, pd.Series(best_silh, index=x.index)

def cluster_kmeans_top(corr: pd.DataFrame, max_num_clusters: int = None, n_init: int = 3) -> Tuple[pd.DataFrame, Dict, pd.Series]:
    """Optimized top-level clustering."""
    max_num_clusters = max_num_clusters or corr.shape[1] - 1
    
    corr1, clusters, silh = cluster_kmeans_base(corr, max_num_clusters, n_init)
    
    cluster_tstats = {i: silh[clusters[i]].mean() / silh[clusters[i]].std() 
                     if silh[clusters[i]].std() != 0 else float('-inf')
                     for i in clusters}
    
    tstat_mean = np.mean(list(cluster_tstats.values()))
    redo_clusters = [i for i, stat in cluster_tstats.items() if stat < tstat_mean]
    
    if len(redo_clusters) <= 1:
        return corr1, clusters, silh
        
    keys_redo = [col for i in redo_clusters for col in clusters[i]]
    corr_tmp = corr.loc[keys_redo, keys_redo]
    
    if corr_tmp.shape[0] <= 2:  # Handle edge case
        return corr1, clusters, silh
        
    corr2, clusters2, silh2 = cluster_kmeans_top(corr_tmp, max_num_clusters, n_init)
    
    # Combine results
    clusters_new = {i: clusters[i] for i in clusters if i not in redo_clusters}
    clusters_new.update({len(clusters_new) + i: cluster 
                        for i, cluster in clusters2.items()})
    
    new_idx = [col for cluster in clusters_new.values() for col in cluster]
    corr_new = corr.loc[new_idx, new_idx]
    
    x = np.sqrt((1 - corr.fillna(0)) / 2.)
    kmeans_labels = np.zeros(len(x.columns))
    for i, cluster in clusters_new.items():
        idx = [x.index.get_loc(k) for k in cluster]
        kmeans_labels[idx] = i
    
    silh_new = pd.Series(silhouette_samples(x, kmeans_labels), index=x.index)
    
    new_tstat = np.mean([silh_new[cluster].mean() / silh_new[cluster].std() 
                        if silh_new[cluster].std() != 0 else float('-inf')
                        for cluster in clusters_new.values()])
                        
    return (corr_new, clusters_new, silh_new) if new_tstat > tstat_mean else (corr1, clusters, silh)

def random_block_corr(n_cols: int, n_blocks: int, min_block_size: int = 1, 
                     random_state: int = None) -> pd.DataFrame:
    """Optimized random block correlation matrix generation."""
    rng = check_random_state(random_state)
    max_val = n_cols - (min_block_size - 1) * n_blocks
    
    if max_val <= 1:
        raise ValueError("Invalid parameters: resulting matrix would be too small")
        
    parts = np.sort(rng.choice(range(1, max_val), n_blocks - 1, replace=False))
    parts = np.diff(np.concatenate(([0], parts, [max_val]))) + min_block_size
    
    covs = [get_cov_sub(int(max(n * (n + 1) / 2, 100)), n, 0.5, rng) 
            for n in parts]
    
    cov = block_diag(*covs)
    cov += get_cov_sub(n_cols, n_cols, 1.0, rng)  # Add noise
    
    return pd.DataFrame(cov2corr(cov))

def get_cov_sub(n_obs: int, n_cols: int, sigma: float, 
                random_state: np.random.RandomState = None) -> np.ndarray:
    """Optimized sub-correlation matrix generation."""
    rng = random_state or np.random.RandomState()
    ar0 = rng.normal(size=(n_obs, 1))
    ar0 = np.tile(ar0, (1, n_cols))
    ar0 += rng.normal(scale=sigma, size=ar0.shape)
    return np.cov(ar0, rowvar=False)

def cov2corr(cov: np.ndarray) -> np.ndarray:
    """Optimized covariance to correlation conversion."""
    std = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std, std)
    np.clip(corr, -1, 1, out=corr)
    return corr