# Generated from: multivariate_cointegration.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# References: 
#
# - [Galenko, A., Popova, E., and Popova, I. (2012). **Trading in the presence of cointegration.** *The Journal of Alternative Investments*, 15(1):85–97.](http://www.ntuzov.com/Nik_Site/Niks_files/Research/papers/stat_arb/Galenko_2007.pdf)


# # Multivariate Cointegration Framework


# ## Introduction


# The cointegration relations between time series imply that the time series are bound together. Over time the time series
# might drift apart for a short period of time, but they ought to re-converge. A trading strategy on $N \: (N \geq 3)$ cointegrated assets that have a positive expectation of profit can be designed based on this property. 
#
# In this notebook, the trading strategy will be demonstrated, and an empirical example of applying this strategy to four European stock indices will be given.


# ## Multivariate Cointegration


# Cointegration is defined by the stochastic relationships among the asset log returns.
#
# Let $P_i$, where $i = 1, 2, \ldots, N$ denote the price of $N$ assets. The continuously compounded asset
# returns, i.e. log-returns at time $t > 0$ can be written as:
#
# \begin{equation*}
# r_t^i = \ln{P_t^i} - \ln{P_{t-1}^i}
# \end{equation*}
#
# Now construct a process $Y_t$ as a linear combination of the $N$ asset prices:
#
# \begin{equation*}
# Y_t = \sum_{i=1}^N b^i \ln{P_t^i}
# \end{equation*}
#
# where $b^i$ denotes the $i$-th element for a finite vector $\mathbf{b}$.
#
# The corresponding asset returns series $Z_t$ can be defined as:
#
# \begin{equation*}
# Z_t = Y_t - Y_{t-1} = \sum_{i=1}^N b^i r_t^i
# \end{equation*}
#
# Assume that the memory of the process $Y_t$ does not extend into the infinite past, which can be expressed as the
# following expression in terms of the autocovariance of the process $Y_t$:
#
# \begin{equation*}
# \lim_{p \to \infty} \text{Cov} \lbrack Y_t, Y_{t-p} \rbrack = 0
# \end{equation*} 
#
# Then the **log-price** process $Y_t$ is stationary, if and only if the following three conditions on
# **log-returns** process $Z_t$ are satisfied:
#
# \begin{gather*}
# E[Z_t] = 0 \\
# \text{Var }Z_t = -2 \sum_{p=1}^{\infty} \text{Cov} \lbrack Z_t, Z_{t-p} \rbrack \\
# \sum_{p=1}^{\infty} p \text{ Cov} \lbrack Z_t, Z_{t-p} \rbrack < \infty
# \end{gather*}
#
# When $Y_t$ is stationary, the log-price series of the assets are cointegrated.
#
# For equity markets, the log-returns time series can be assumed as stationary and thus satisfy the above conditions.
# Therefore, when it comes to empirical applications, the Johansen test could be directly applied to the log price series
# to derive the vector $\mathbf{b}$.


# ## Trading Strategy


# The core idea of the strategy is to bet on the spread formed by the cointegrated $N$ assets that have gone apart
# but are expected to mean revert in the future.
#
# The trading strategy, using the notation in the above section, can be described as follows.
#
# 1. Estimate the cointegration vector $\hat{\mathbf{b}}$ with Johansen test using training data.
# 2. Construct the realization $\hat{Y}_t$ of the process $Y_t$ by calculating $\hat{\mathbf{b}}^T \ln P_t$, and calculate $\hat{Z}_t = \hat{Y}_t - \hat{Y}_{t-1}$.
# 3. Compute the finite sum $\sum_{p=1}^P \hat{Z}_{t-p}$, where the lag $P$ is an input argument.
# 4. Partition the assets into two sets $L$ and $S$ according to the sign of the element in the cointegration vector $\hat{\mathbf{b}}$. For each asset $i$,
#
# \begin{eqnarray*}
# i \in L \iff b^i \geq 0 \\
# i \in S \iff b^i < 0
# \end{eqnarray*}
#
# 5. Following the formulae below, calculate the number of assets to trade so that the notional of the positions would equal to $C$.
#
# \begin{eqnarray*}
#     \Bigg \lfloor \frac{-b^i C \text{ sgn} \bigg( \sum_{p=1}^{P} Z_{t-p} \bigg)}{P_t^i \sum_{j \in L} b^j} \Bigg \rfloor, \: i \in L \\
#     \Bigg \lfloor \frac{b^i C \text{ sgn} \bigg( \sum_{p=1}^{P} Z_{t-p} \bigg)}{P_t^i \sum_{j \in L} b^j} \Bigg \rfloor, \: i \in S
# \end{eqnarray*}
#
# 6. Open the positions on time $t$ and close the positions on time $t+1$.
# 7. Update the training data with the closing price.
# 8. The cointegration vector will be re-estimated monthly (22 trading days). If it is time for a re-estimate, go to step 1; otherwise, go to step 2.
#
# The strategy is trading at daily frequency and always in the market.


# ## Usage of the Module


# In this section, the usage of multivariate cointegration trading strategy will be demonstrated with an empirical example of four European stock indices, i.e. DAX (Germany), CAC 40 (France), FTSE 100 (UK), and AEX (Netherlands). Price history from Jan 2nd, 1996 to Dec 28th, 2006 was used. The module allows two missing data imputation methods: forward-fill and polynomial spline. In the following demonstration, missing data due to the difference in working days in different countries was imputed with a forward-fill method in order to avoid the introduction of phantom returns on non-trading days.
#
# Trading for out-of-sample tests starts on Nov 6th, 2001 and ends on Dec 28th, 2006. The cointegration vector $\mathbf{b}$ was re-estimated monthly (every 22 trading days) using the Johansen test. The notional value of the long positions and short positions each day was set to $\$10 \text{M}$, respectively. To be specific, each day $\$10 \text{M}$ were invested in longs and another $\$10 \text{M}$ were invested in shorts, resulting in a $\$20 \text{M}$ portfolio.


%matplotlib inline


# Importing libraries
import pandas as pd
import numpy as np

from arbitragelab.cointegration_approach.multi_coint import MultivariateCointegration


# Loading data
euro_stocks_df = pd.read_csv("multi_coint.csv", parse_dates=['Date'])
euro_stocks_df.set_index("Date", inplace=True)

# Out-of-sample data split time point
split_point = pd.Timestamp(2001, 11, 6)

# Indexing with DateTimeIndex is always inclusive. Removing the last data point in the training data
train_df = euro_stocks_df.loc[:split_point].iloc[:-1]
trade_df = euro_stocks_df.loc[split_point:]


# Checking train data
train_df.tail()


# Checking test data
trade_df.head()


# ### Generate Trading Signal and Equity Curve


# In this section, a few experiments will be done to showcase the following:
#
# - In-sample test of the strategy with a rolling window.
# - In-sample test of the strategy with a cumulative window.
# - Out-of-sample test of the strategy with a rolling window.
# - Out-of-sample test of the strategy with a cumulative window.
#
# A lag of 30 days will be used across four experiments to calculate the signals.
#
# For the in-sample test, the cointegration vector will be estimated with all available data (including training and test data) and will not be updated monthly. 
#
# For the out-of-sample test, since the cointegration vector will be re-estimated every month, the time evolution of the cointegration vector will be shown as well as the number of shares to trade. We gave two examples, one of which displays the raw number of shares, the other the weight of portfolio notional value. Positive values indicate long positions, while negative values indicate short positions.
#
# The equity curve and the statistics of the returns are shown for each experiment.


# Initializing the trading signal generator
multi_coint_signal = MultivariateCointegration(train_df, trade_df)

# Imputing all missing values
multi_coint_signal.fillna_inplace(nan_method='ffill')


# ### 1) In-sample, rolling window of 1500 days


# Generating the signal, recording the cointegration vector time evolution and calculating portfolio returns
signal, _, coint_vec, port_returns = multi_coint_signal.trading_signal(nlags=30, rolling_window_size=1500, insample=True)


# Plotting the equity curve
plot = multi_coint_signal.plot_returns(port_returns, start_date=pd.Timestamp(2001, 11, 6), end_date=pd.Timestamp(2007, 1, 2),
                                       figw=15, figh=10, title="In-sample Test, 1500-day Rolling Window")


# Returns statistics
multi_coint_signal.summary(port_returns)


# ### 2) In-sample, cumulative window


# Generating the signal, recording the cointegration vector time evolution and calculating portfolio returns
signal, _, coint_vec, port_returns = multi_coint_signal.trading_signal(nlags=30, rolling_window_size=None, insample=True)


# Plotting the equity curve
plot = multi_coint_signal.plot_returns(port_returns, start_date=pd.Timestamp(2001, 11, 6), end_date=pd.Timestamp(2007, 1, 2),
                                       figw=15, figh=10, title="In-sample Test, Cumulative Window")


# Returns statistics
multi_coint_signal.summary(port_returns)


# ### 3) Out-of-sample, rolling window of 1500 days


# Generating the signal, recording the cointegration vector time evolution and calculating portfolio returns
signal, signal_ntn,  coint_vec, port_returns = multi_coint_signal.trading_signal(nlags=30, rolling_window_size=1500, 
                                                                                 insample=False)


# An example of trading signals in notional value will look as follows:


signal_ntn.head()


# Display the weight of portfolio notional value to invest for each equity index. The plot function will automatically normalize the weights with respect to the sum of long notional and short notional value.


# Plotting the equity curve, cointegration vectors, and trading signals
plot = multi_coint_signal.plot_all(signal, signal_ntn, coint_vec, port_returns,
                                   start_date=pd.Timestamp(2001, 11, 6), end_date=pd.Timestamp(2007, 1, 2),
                                   title="Out-of-sample Test, 1500-day Rolling Window", use_weights=True)


# Returns statistics
multi_coint_signal.summary(port_returns)


# ### 4) Out-of-sample, cumulative window


# Generating the signal, recording the cointegration vector time evolution and calculate portfolio returns
signal, signal_ntn, coint_vec, port_returns = multi_coint_signal.trading_signal(nlags=30, rolling_window_size=None, 
                                                                                insample=False)


# Display the raw number of shares to trade.


signal.head()


# Plot the equity curve, cointegration vectors, and trading signals
plot = multi_coint_signal.plot_all(signal, signal_ntn, coint_vec, port_returns,
                                   start_date=pd.Timestamp(2001, 11, 6), end_date=pd.Timestamp(2007, 1, 2),
                                   title="Out-of-sample Test, 1500-day Rolling Window")


# Returns statistics
multi_coint_signal.summary(port_returns)


# ## Discussion


# The result of the above experiments has shown that the rolling window setup is better than the cumulative window setup. Also, re-estimating the cointegration vector monthly improves the performance of the strategy, as the out-of-sample test outperformed. Both of these results suggest that it is better to exclude further history when estimating the cointegration vector, as the cointegration relationship between the $N$ assets are time-varying. It also provides circumstantial evidence that the following assumptions of the model are reasonable:
#
# \begin{eqnarray*}
# \lim_{p \to \infty} \text{Cov} \lbrack Y_t, Y_{t-p} \rbrack = 0 \\
# \sum_{p=1}^{\infty} p \text{ Cov} \lbrack Z_t, Z_{t-p} \rbrack < \infty
# \end{eqnarray*}
#
# These two assumptions indicate that long-term memory for the cointegrated assets will be almost non-existent. 
#
# However, this trading strategy also has its limitations. Since the index value of AEX is much smaller than DAX, FTSE, and CAC 40, the number of AEX shares/contracts that need to be traded is much larger than its counterpart. Therefore, when the prices of the assets are different in the order of magnitude, it is better to double-check the position limit before trading the strategy.


# ## Conclusion


# This notebook demonstrated a profitable trading strategy using the properties of cointegration among $N$ assets. An empirical example of trading four European stock indices (AEX, DAX, FTSE, and CAC) has shown that: using a lookback of 30 trading days and re-estimating cointegration vector monthly with a 1500-day rolling window, the trading strategy was able to yield a cumulative return of 42.7%, the returns distribution of the strategy did not have significant skewness and kurtosis, and the strategy achieved a Sharpe ratio of 1.31 and a Sortino ratio of 1.85.
#
# ### Key Takeaways
#
# - The cointegration relation can be defined by the properties of compounded returns rather than asset prices.
# - It is possible to trade a strategy that has positive profit expectancy based on this cointegration relation of $N$ assets.


# ## Reference


# 1. [Galenko, A., Popova, E. and Popova, I., 2012. Trading in the presence of cointegration. The Journal of Alternative Investments, 15(1), pp.85-97.](http://www.ntuzov.com/Nik_Site/Niks_files/Research/papers/stat_arb/Galenko_2007.pdf)

