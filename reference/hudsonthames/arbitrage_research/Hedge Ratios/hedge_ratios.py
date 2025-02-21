# Generated from: hedge_ratios.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from arbitragelab.hedge_ratios import (construct_spread, get_box_tiao_hedge_ratio,
                                       get_johansen_hedge_ratio, get_minimum_hl_hedge_ratio, 
                                       get_ols_hedge_ratio, get_tls_hedge_ratio,
                                       get_adf_optimal_hedge_ratio)


# # Hedge Ratio Methods


# In order to test our hedge ratios module, let's first create a spread that is mean-reverting by its nature and see how different methods perform.


# Generating a series of returns X
rs = np.random.RandomState(42)
X_returns = rs.normal(0, 1, 100)
X = pd.Series(np.cumsum(X_returns), name='X') + 50

# And series of cointegrated returns Y
noise = rs.normal(0, 1, 100)
Y = 5 * X + noise
Y.name = 'Y'

cointegrated_series = pd.concat([Y, X], axis=1)


# By default, the first columns ticker is used as a **dependent variable**. This can be adjusted in hedge ratio functions by providing an alternative ticker to be used as a dependent variable.


# Check columns in a generated dataframe
cointegrated_series.columns


# Use the construct_spread function with provided hedge ratios
theoretical_spread = construct_spread(price_data=cointegrated_series,
                                      hedge_ratios={'Y': 1, 'X': 5})


# Plot resulting spread
theoretical_spread.plot(figsize=(12, 10), grid=True, title='Cointegrated spread series.');


# One can also decide on `dependent variable` in `construct_spread` function.


# Spread construction with given dependent variable
theoretical_spread_reverted = construct_spread(price_data=cointegrated_series,
                                               hedge_ratios={'Y': 1, 'X': 5},
                                               dependent_variable='X')

theoretical_spread_reverted.plot(figsize=(12, 10), grid=True, title='Cointegrated spread series with X being dependent variable.');


# Now we can compare these spreads and see that one is a reverted version of the other.


theoretical_spread_reverted.plot(figsize=(12, 10), grid=True, title='Spreads comparison.')
theoretical_spread.plot(figsize=(12, 10), grid=True, title='Spreads comparison.');


# Mean values of two generated spreads
theoretical_spread.mean(), theoretical_spread_reverted.mean()


# ## OLS and TLS hedge ratios


# Now let's use Ordinary Least Squares and Total Least Squares to estimate hedge ratios and see how far the results are from theoretical values.


ols_hedge_ratio, X, y, spread_ols = get_ols_hedge_ratio(price_data=cointegrated_series,
                                                        dependent_variable='Y',
                                                        add_constant=False) # One can add constant if needed.

tls_hedge_ratio, X, y, spread_tls = get_tls_hedge_ratio(price_data=cointegrated_series,
                                                        dependent_variable='Y',
                                                        add_constant=False) # One can add constant if needed.


# Hedge ratios methods return:
# - Hedge ratio dictionary such that the `dependent variable` has a hedge ratio of 1. 
# - X and y datasets used in model valuation. It means that the ratio was found by regressing $y \sim X + eps$.
# - Resulting spread obtained by calculated hedge ratio. It can be also obtained by using `contruct_spread` method.
# - All hedge ratio and spread calculations assume that: $spread = 1.0*Price_{dependent variable} - hedge_{1}*Price_{1}-...hedge_{n}*Price_{n}$


# Checking hedge reatios for both methods
ols_hedge_ratio, tls_hedge_ratio


# As we can see, OLS and TLS managed to capture the hedge ratio correctly.


# Plotting theoretical, OLS, and TLS spreads

theoretical_spread.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='Theoretical spread.')
spread_ols.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='OLS spread')
spread_tls.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='TLS spread.')
plt.legend(loc='best');


# ## Johansen hedge ratio


johansen_hedge_ratio, _, _, spread_joh = get_johansen_hedge_ratio(price_data=cointegrated_series,
                                                                  dependent_variable='Y')


# Checking hedge reatio of the Johansen method
johansen_hedge_ratio


# ## Box-Tiao hedge ratio


bt_hedge_ratio, _, _, spread_bt = get_box_tiao_hedge_ratio(price_data=cointegrated_series,
                                                           dependent_variable='Y')


# Checking hedge reatio of the Box-Tiao method
bt_hedge_ratio


# ## Minimum half-life, Minimum ADF t-statistic hedge ratio


# Min HL, Min ADF methods use numerical optimization techniques to find a spread with minimum half-life of mean-reversion, minimum ADF
# t-statistic, respectively.


min_hl_hedge_ratio, _, _, spread_min_hl, opt_object_hl = get_minimum_hl_hedge_ratio(price_data=cointegrated_series, 
                                                                                    dependent_variable='Y')

min_adf_hedge_ratio, _, _, spread_min_adf, opt_object_adf = get_adf_optimal_hedge_ratio(price_data=cointegrated_series, 
                                                                                        dependent_variable='Y')


# Checking hedge reatio of the Minimum half-life method
min_hl_hedge_ratio


# Checking hedge reatio of the Minimum ADF t-statistic method
min_adf_hedge_ratio


# As both methods rely on numerical optimization, sometimes methods fail to converge yielding unstable, wrong results. That is why both methods return scipy optimization objects which can be used to check the status of optimization.


# Optimization status of the Minimum half-life method
opt_object_hl.message


# Optimization status of the Minimum ADF t-statistic method
opt_object_adf.message


# ## Example of diverging min HL/ADF hedge ratios


diverging_series = cointegrated_series.copy()

# Creating two constant assets.
diverging_series['Y'] = 1.0
diverging_series['X'] = 2.0


min_hl_hedge_ratio, _, _, spread_min_hl, opt_object_hl = get_minimum_hl_hedge_ratio(price_data=diverging_series, 
                                                                                    dependent_variable='Y')

min_adf_hedge_ratio, _, _, spread_min_adf, opt_object_adf = get_adf_optimal_hedge_ratio(price_data=diverging_series, 
                                                                                        dependent_variable='Y')


# Optimization status of both methods
opt_object_hl.message, opt_object_adf.message


# ## Example on real data


# Let's apply functions on a real dataset and construct a spread from 3 assets.


# Loading data
price_data = pd.read_csv('data/data.csv', index_col=0, parse_dates=[0])
price_data = price_data[['GOOG', 'AAPL', 'AMZN']].dropna()


# Calculating hedge ratios using all mehtods

ols_hedge_ratio, _, _, spread_ols = get_ols_hedge_ratio(price_data=price_data, dependent_variable='GOOG', add_constant=False) 
tls_hedge_ratio, _, _, spread_tls = get_tls_hedge_ratio(price_data=price_data, dependent_variable='GOOG', add_constant=False)
joh_hedge_ratio, _, _, spread_joh = get_johansen_hedge_ratio(price_data=price_data, dependent_variable='GOOG')
bt_hedge_ratio, _, _, spread_bt = get_box_tiao_hedge_ratio(price_data=price_data, dependent_variable='GOOG')
min_hl_hedge_ratio, _, _, spread_min_hl, _ = get_minimum_hl_hedge_ratio(price_data=price_data, dependent_variable='GOOG')
min_adf_hedge_ratio, _, _, spread_min_adf, _ = get_adf_optimal_hedge_ratio(price_data=price_data, dependent_variable='GOOG')


# Plotting spreads from each method
spread_ols.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='OLS spread')
spread_tls.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='TLS spread.')
spread_joh.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='Johansen spread')
spread_bt.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='Box-Tiao spread')
spread_min_hl.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='Min HL spread')
spread_min_adf.plot(figsize=(12, 10), grid=True, title='Spreads comparison', label='Min ADF spread')
plt.legend(loc='best');


# ## Conclusion
#
# This notebook presents the use of the hedge ratios methods available in the MlFinLab package. 
#
# When applied to synthetically generated data, they perform similarly. However, on real data, the results may differ, as methods have different underlying logic.
#
# It should be noted that some methods may fail to converge, and the output may be unstable.

