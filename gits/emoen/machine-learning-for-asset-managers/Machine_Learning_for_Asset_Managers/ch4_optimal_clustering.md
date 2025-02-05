# Documentation for `ch4_optimal_clustering.py`

## Overview

This script implements the Optimal Number of Clusters (ONC) algorithm for detecting false investment strategies using unsupervised learning methods. It employs K-Means clustering on correlation matrices.

### Functions

- **clusterKMeansBase(corr0, maxNumClusters=10, n_init=10, debug=False)**: Performs K-Means clustering on a correlation matrix, evaluates silhouette scores, and determines optimal clusters.

- **makeNewOutputs(corr0, clstrs, clstrs2)**: Generates new outputs based on improved cluster elements and recalculates silhouette scores.

- **clusterKMeansTop(corr0, maxNumClusters=None, n_init=10)**: Recursively clusters the correlation matrix and refines clusters based on silhouette statistics.

- **getCovSub(nObs, nCols, sigma, random_state=None)**: Generates a covariance matrix for a set of normally distributed random variables.

- **getRndBlockCov(nCols, nBlocks, minBlockSize=1, sigma=1., random_state=None)**: Creates a block diagonal covariance matrix with specified blocks.

- **randomBlockCorr(nCols, nBlocks, random_state=None, minBlockSize=1)**: Constructs a random block correlation matrix from two covariance matrices.

### Main Execution

The script generates a random block correlation matrix, applies K-Means clustering, and visualizes both the original and clustered correlation matrices.