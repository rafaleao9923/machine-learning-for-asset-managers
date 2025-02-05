# Documentation for `ch8_testing_set_overfitting.py`

## Overview

This script tests for overfitting and selection bias in financial strategies using statistical methods. It implements the theoretical framework from the paper "The Deflated Sharpe Ratio" by David H. Bailey and Marcos López de Prado.

### Functions

- **getExpectedMaxSR(nTrials, meanSR, stdSR)**: Computes the expected maximum Sharpe Ratio.

- **getDistMaxSR(nSims, nTrials, stdSR, meanSR)**: Performs Monte Carlo simulations to estimate the distribution of the maximum Sharpe Ratio.

- **getMeanStdError(nSims0, nSims1, nTrials, stdSR=1, meanSR=0)**: Calculates the mean and standard deviation of prediction errors across trials.

- **getZStat(sr, t, sr_=0, skew=0, kurt=3)**: Computes the Z-statistic for the Sharpe Ratio.

- **type1Err(z, k=1)**: Calculates the Type I error rate (false positives).

- **getTheta(sr, t, sr_=0., skew=0., kurt=3)**: Computes the theta value used in Type II error calculations.

- **type2Err(alpha_k, k, theta)**: Calculates the Type II error rate (false negatives).

### Main Execution

The script generates statistical plots for the maximum Sharpe Ratio and calculates Type I and Type II error rates based on simulated data.