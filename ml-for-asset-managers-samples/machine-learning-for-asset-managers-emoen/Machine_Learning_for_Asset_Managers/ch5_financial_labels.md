# Documentation for `ch5_financial_labels.py`

## Overview

This script implements a trend scanning method using linear regression to derive labels based on the significance of trends in financial time series data.

### Functions

- **tValLinR(close)**: Computes the t-statistic for the slope of a linear trend fitted to the closing prices.

- **getBinsFromTrend(molecule, close, span)**: Derives labels from the sign of the t-value of the trend line. Outputs include:
  - `t1`: End time for the identified trend.
  - `tVal`: t-value associated with the estimated trend coefficient.
  - `bin`: Sign of the trend.

### Main Execution

The script generates a synthetic time series, applies the trend scanning method, and visualizes the results. An optional normalization of t-values is included.