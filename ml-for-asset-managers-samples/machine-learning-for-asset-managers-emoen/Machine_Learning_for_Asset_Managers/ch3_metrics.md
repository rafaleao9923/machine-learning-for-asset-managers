# Documentation for `ch3_metrics.py`

## Overview

```python
# Marginal-, joint-distribution, conditional entropies, and mutual information
# https://pypi.org/project/pyitlib/
```

This script calculates various metrics related to the entropies and mutual information of random variables, including variation of information and normalized mutual information.

### Functions

- **numBins(nObs, corr=None)**: Determines the optimal number of bins for discretizing continuous random variables.

- **varInfo(x, y, bins, norm=False)**: Computes the variation of information between two random variables.

- **mutualInfor(x, y, norm=False)**: Calculates the mutual information between two random variables, with an option for normalization.

### Main Execution

The script simulates a pair of independent normal random variables and computes their mutual information, variation of information, and other related metrics.