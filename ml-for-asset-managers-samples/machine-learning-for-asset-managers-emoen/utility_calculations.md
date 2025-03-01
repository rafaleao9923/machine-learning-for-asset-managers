# Documentation for `utility_calculations.py`

## Overview

This script contains utility functions for calculating the correlation and covariance of stock prices. The focus is on implementing these calculations using NumPy and Pandas.

### Functions

- **calculate_correlation(S, T=936, N=234)**: Computes the correlation matrix from the stock price data.

- **correlation_from_covariance(covariance)**: Converts a covariance matrix into a correlation matrix.

### Main Execution

The script loads stock prices from a CSV file, calculates their percentage returns, and then computes the correlation matrix based on these returns.