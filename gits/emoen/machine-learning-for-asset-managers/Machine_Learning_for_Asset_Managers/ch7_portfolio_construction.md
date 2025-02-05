# Documentation for `ch7_portfolio_construction.py`

## Overview

This script implements portfolio construction techniques using a combination of convex optimization and clustering methods to allocate assets based on their covariance and expected returns.

### Functions

- **minVarPort(cov)**: Computes the minimum variance portfolio given a covariance matrix.

- **optPort_nco(cov, mu, maxNumClusters)**: Implements the NCO (Nested Clustering Optimization) algorithm to optimize portfolio allocations based on a clustered covariance matrix.

- **allocate_cvo(cov, mu_vec)**: Estimates the Convex Optimization Solution (CVO) for optimal asset allocation, maximizing the Sharpe ratio or minimizing variance.

### Main Execution

The script generates block-diagonal correlation matrices, clusters the correlation matrix, computes intra-cluster and inter-cluster allocations, and evaluates allocation errors using simulated data.