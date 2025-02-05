# Documentation for `ch2_monte_carlo_experiment.py`

## Overview

```python
#optPort with long only curtesy of Brady Preston
#requires: import cvxpy as cp
'''def optPort(cov,mu=None):
    n = cov.shape[0]
    if mu is None:mu = np.abs(np.random.randn(n, 1))
    w = cp.Variable(n)
    risk = cp.quad_form(w, cov)
    ret =  mu.T @ w
    constraints = [cp.sum(w) == 1, w >= 0]
    prob = cp.Problem(cp.Minimize(risk),constraints)
    prob.solve(verbose=True)
    return np.array(w.value.flat).round(4)'''
```

This script performs a Monte Carlo experiment to simulate and analyze the behavior of asset returns using a block-diagonal covariance structure.

### Functions

- **formBlockMatrix(nBlocks, bSize, bCorr)**: Generates a block-diagonal covariance matrix with specified block size and correlation.

- **formTrueMatrix(nBlocks, bSize, bCorr)**: Creates a true mean vector and covariance matrix. It shuffles the columns of the correlation matrix.

- **corr2cov(corr, std)**: Converts a correlation matrix to a covariance matrix using a given standard deviation vector.

- **simCovMu(mu0, cov0, nObs, shrink)**: Simulates observations from a multivariate normal distribution and computes the empirical mean and covariance matrix.

- **deNoiseCov(cov0, q, bWidth)**: Denoises the empirical covariance matrix using the constant residual eigenvalue method.

- **optPort(cov, mu)**: Calculates the minimum variance portfolio weights based on the covariance matrix and expected returns.

- **optPortLongOnly(cov, mu)**: Calculates the minimum variance portfolio weights while enforcing a long-only constraint.

### Main Execution

The script generates a block-diagonal covariance matrix, simulates asset returns, computes empirical covariance, and evaluates the performance of the denoised covariance matrix against the true covariance matrix using RMSE.