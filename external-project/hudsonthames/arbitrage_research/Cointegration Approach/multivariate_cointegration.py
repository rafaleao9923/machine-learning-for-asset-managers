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
# 7. Every once in a while - once per month (22 trading days) for example, re-estimate the cointegration vector. If it is time for a re-estimate, go to step 1; otherwise, go to step 2.
#
#
# The strategy is trading at daily frequency and always in the market.


# ## Usage of the Module


# In this section, the usage of multivariate cointegration trading strategy will be demonstrated with an empirical example of four European stock indices, i.e. DAX (Germany), CAC 40 (France), FTSE 100 (UK), and AEX (Netherlands). Price history from Jan 2nd, 1996 to Dec 28th, 2006 was used. The module allows two missing data imputation methods: forward-fill and polynomial spline. In the following demonstration, missing data due to the difference in working days in different countries was imputed with a forward-fill method in order to avoid the introduction of phantom returns on non-trading days.
#
# Trading for out-of-sample tests starts on Nov 6th, 2001 and ends on Dec 28th, 2006. The cointegration vector $\mathbf{b}$ was estimated using the Johansen test. The notional value of the long positions and short positions each day was set to $\$10 \text{M}$, respectively. To be specific, each day $\$10 \text{M}$ were invested in longs and another $\$10 \text{M}$ were invested in shorts, resulting in a $\$20 \text{M}$ portfolio.


%matplotlib inline


# Importing libraries
import pandas as pd
import numpy as np

from arbitragelab.cointegration_approach.multi_coint import MultivariateCointegration
from arbitragelab.trading import MultivariateCointegrationTradingRule


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


# ### Optimize and Generate Trading Signal


# For the following test, the cointegration vector will be estimated with all training data and will not be updated monthly, but this can easily be made by re-running the MultivariateCointegration optimization.


# Initializing the optimizer
optimizer = MultivariateCointegration()

# Set the trainging deatset
optimizer.set_train_dataset(train_df)

# Imputing all missing values
optimizer.fillna_inplace(nan_method='ffill')


# Generating the cointegration vector to later use in a trading strategy
coint_vec = optimizer.get_coint_vec()


# Now we can now use the MultivariateCointegrationTradingRule from the Spread Trading module to feed in new price values and get signls - number of shares to trade per asset. With the mechanism of providing price values one by one to the strategy, it's easier to integrate this strategy in an existing trading pipeline.


# Creating a strategy
strategy = MultivariateCointegrationTradingRule(coint_vec)


# Now we use a loop to simulate a live data feed.


# Adding initial price values
strategy.update_price_values(trade_df.iloc[0])

# Feeding price values to the strategy one by one
for ind in range(trade_df[:5].shape[0]):

    time = trade_df.index[ind]
    value = trade_df.iloc[ind]

    strategy.update_price_values(value)

    # Getting signal - number of shares to trade per asset
    pos_shares, neg_shares, pos_notional, neg_notional = strategy.get_signal()

    # Close previous trade
    strategy.update_trades(update_timestamp=time)

    # Add a new trade
    strategy.add_trade(start_timestamp=time, pos_shares=pos_shares, neg_shares=neg_shares)


# Currently open trades in a strategy
open_trades = strategy.open_trades

open_trades


# Only one trade is io all trades but one were closed.


# Checking all closed trades
closed_trades = strategy.closed_trades

closed_trades


# We see the closed trades with signals - a number of shares to trade for each set of prices in our testing dataset.
#
# ### Strategy outputs
#
# We can see the following data:
# * Dictionary key:
#     * Timestamp at which the trade was opened
# * Dctionary value:
#     * t1: Timestamp at which the trade was closed
#     * pt: Prices at which the trade was closed
#     * uuid: Trade ID that can be provided for each trade
#     * start_prices: Prices at which spread was opened
#     * end_prices: Prices at which spread was closed
#     * pos_shares: Ticker and number of shares to go long
#     * neg_shares: Ticker and number of shares to go short 


# ## Discussion


# In general, from the conducted experiments, we discovered that the rolling window setup is better than the cumulative window setup. Also, re-estimating the cointegration vector monthly improves the performance of the strategy. It is better to exclude further history when estimating the cointegration vector, as the cointegration relationship between the $N$ assets are time-varying. It also provides circumstantial evidence that the following assumptions of the model are reasonable:
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


# This notebook demonstrated a trading strategy using the properties of cointegration among $N$ assets, and included an empirical example of trading four European stock indices (AEX, DAX, FTSE, and CAC).
#
# ### Key Takeaways
#
# - The cointegration relation can be defined by the properties of compounded returns rather than asset prices.
# - It is possible to trade a strategy that has positive profit expectancy based on this cointegration relation of $N$ assets.


# ## Reference


# 1. [Galenko, A., Popova, E. and Popova, I., 2012. Trading in the presence of cointegration. The Journal of Alternative Investments, 15(1), pp.85-97.](http://www.ntuzov.com/Nik_Site/Niks_files/Research/papers/stat_arb/Galenko_2007.pdf)

