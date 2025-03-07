# Generated from: basic_distance_approach.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# * Reference: __Pairs Trading: Performance of a Relative Value Arbitrage Rule__ _by_ Gatev et al.


# # Distance Approach


# This description of the distance approach closely follows the paper by _Gatev, E., Goetzmann, W. N.,_ and _Rouwenhorst, K. G._ __Pairs Trading: Performance of a Relative Value Arbitrage Rule__  [available here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=141615). 


# ## Introduction


# The distance approach works as follows:
# - First, a historical period is defined, cumulative returns for assets in this period are normalized.
# - Second, using the Euclidean squared distance on the normalized price time series, $n$ closest pairs of assets are picked.
# - After the pairs are formed, the trading period starts, and the trading signals are generated. The mechanism
#   behind this process if the following:
#   - If the difference between the price of elements in a pair diverged by
#     more than 2 standard deviations (calculated for each pair during the training period), the positions are
#     opened - long for the element with a lower price in a portfolio and short for an element with a higher price
#     in a portfolio.
#   - These positions are closed when the normalized prices cross or when the trading period ends.
#
# Using this standard description, the distance approach is a parameter-free strategy.
#
# **Note:** No cointegration tests (as opposed to the mean reversion approach) are being performed in the distance
# approach. As spotted in the work by Krauss (2015), dependencies found using this approach can be spurious.
# This also leads to higher divergence risks, and as shown in the work by Do and Faff (2010), up to 32% of
# pairs identified by this method are not converging.
#
# There are, however, possible adjustments to this strategy, like choosing distances other from the Euclidean
# square distance, adjusting the threshold to enter a trade for each pair, etc. 


# ## Pairs formation step
#
# This stage of the DistanceStrategy consists of the following steps:
#
# 1. **Normalization of the input data.**
#
# To use the Euclidean square distance, the training price time series are being normalized using the following
# formula:
#
# $$P_{normalized} = \frac{P - min(P)}{max(P) - min(P)}$$
#
# where $P$ is the training price series of an asset, $min(P)$ and $max(P)$ are the minimum and maximum values from the price series.
#
# 2. **Finding pairs.**
#
# Using the normalized price series, the distances between each pair of assets are calculated. These
# distances are then sorted in the ascending order and the :math:`n` closest pairs are picked (our
# function also allows skipping a number of first pairs, so one can choose pairs 10-15 to study).
#
# The distances between elements (Euclidean square distance - SSD) are calculated as:
#
# $$SSD = \sum^{N}_{t=1} (P^1_t - P^2_t)^{2}$$
#
# where $P^1_t$ and $P^2_t$ are normalized prices at time $t$ for the first and
# the second elements in a pair.
#
# Using the prices of elements in a pair a portfolio is being constructed - the difference between
# their normalized prices.
#
# 3. **Calculating historical volatility.**
#
# For $n$ portfolios (differences between normalized price series of elements) calculated in the
# previous step, their volatility is being calculated. Historical standard deviations of these portfolios
# will later be used to generate trading signals.


# ## Trading signals generation
#
#
# After pairs were formed, we can proceed to the second stage of the DistanceStrategy - trading
# signals generation. The input to this stage is a dataframe with testing price series for assets - not
# used in the pairs formation stage.
#
# This stage of the DistanceStrategy consists of the following steps:
#
# 1. **Normalization of the input data.**
#
# Using the same approach as in the pairs formation stage, we normalize the input trading dataset using
# the same maximum and minimum historical values from the training price series.
#
# 2. **Portfolios creation.**
#
# In this step, the portfolios are being constructed based on the asset pairs chosen in the pairs
# formation step. Portfolio values series are differences between normalized price series of elements
# in a pair - as we're opening a long position for the first element in a pair and a short position for
# the second element in a pair. A buy signal generated by the strategy means going long on the first
# element and short on the second. A sell signal means the opposite - going short on the first element
# and long on the second element.
#
# 3. **Generating signals.**
#
# If the portfolio value exceeds two historical deviations, a sell signal is generated - we expect
# the price of the first element to decrease and the price of the second element to increase. And if
# the value of the portfolio is below minus two historical deviations, a buy signal is generated.
#
# An open position is closed when the portfolio value crosses the zero mark - or when the prices of
# elements in a pair cross. So at any given time, we have one (buy or sell) or none active positions
# opened. This makes cost allocation for the strategy easier. Resulting trading signals are target
# quantities of portfolios to hold for each pair (with values -1, 0, or +1).


# ## Results output and plotting
#
# The DistanceStrategy class contains multiple methods to get results in the desired form.
#
# Functions that can be used to get data:
#
# - **get_signals()** outputs generated trading signals for each pair.
#
# - **get_portfolios()** outputs values series of each pair portfolios.
#
# - **get_scaling_parameters()** outputs scaling parameters from the training dataset used to normalize data.
#
# - **get_pairs()** outputs a list of tuples, containing chosen top pairs in the pairs formation step.
#
# Functions that can be used to plot data:
#
# - **plot_pair()** plots normalized price series for elements in a given pair and the corresponding
#   trading signals for portfolio of these elements.
#
# - **plot_portfolio()** plots portfolio value for a given pair and the corresponding trading signals.


# ## Usage of the Algorithms


# Let's use the above strategy on real data. 
#
# First, we will choose a training period of 12 months to form pairs. Second, we'll create trading signals for the following 6 months window. Finally, we will analyze the obtained results. 


import arbitragelab as al
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# ### Loading data


# As a dataset we'll download price time series for 176 stocks over a period from 01.2018 to 07.2019. First 12 months of data will be used for training and the following 6 months for trading signal generation and analysis of results. 


# List of tickers to use in the analysis
tickers = ['MMM', 'ABT', 'ANF', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'A', 'APD',
           'AKAM', 'AA', 'ALXN', 'ATI', 'ALL', 'MO', 'AMZN', 'AEE',
           'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AMGN', 'APH', 'ADI', 'AON',
           'APA', 'AIV', 'AAPL', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN',
           'AZO', 'AVB', 'AVY', 'BLL', 'BAC', 'BK', 'BAX', 'BDX', 'BBBY', 'BIG',
           'BIIB', 'BLK', 'HRB', 'BA', 'BWA', 'BXP', 'BSX', 'BMY', 'CHRW', 'COG',
           'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CAT', 'CNP', 'CERN', 'CF', 'SCHW',
           'CVX', 'CMG', 'CB', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLF',
           'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP',
           'CNX', 'ED', 'STZ', 'GLW', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI',
           'DHR', 'DRI', 'DVA', 'DE', 'XRAY', 'DVN', 'DFS', 'DISCA',
           'DLTR', 'D', 'RRD', 'DOV', 'DTE', 'DD', 'DUK', 'ETFC', 'EMN',
           'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', 'EOG', 'EQT',
           'EFX', 'EQR', 'EL', 'EXC', 'EXPE', 'EXPD', 'XOM', 'FFIV', 'FAST', 'FDX',
           'FIS', 'FITB', 'FHN', 'FSLR', 'FE', 'FISV', 'FLIR', 'FLS', 'FLR', 'FMC',
           'FTI', 'F', 'FOSL', 'BEN', 'FCX', 'GME', 'GPS', 'GD', 'GE', 'GIS',
           'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOG', 'GWW', 'HAL', 'HOG', 'HIG',
           'HAS', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HST', 'HUM', 'HBAN',
           'ITW']

# Loading data
train_data =  yf.download(tickers, start="2018-01-03", end="2019-01-01")
test_data =  yf.download(tickers, start="2019-01-02", end="2019-07-01")

# Taking close prices for chosen instruments
train_data = train_data["Adj Close"]
test_data = test_data["Adj Close"]

# Looking at the downloaded data
train_data.head()


# ### Forming pairs


# Now let's form pairs and calculate historical volatilities for chosen portfolio pairs based on training data.


# Initialising an object containing needed methods
strategy = al.distance_approach.DistanceStrategy()

# Performing the pairs formation step and picking top 20 pairs
strategy.form_pairs(train_data, num_top=20)

# Getting scaling values used to normalize data, a list of created pairs and historical volatility for each chosen pair portfolio
scaling_parameters = strategy.get_scaling_parameters()
pairs = strategy.get_pairs()
historical_std = strategy.train_std


# Looking at the scaling parameters 
scaling_parameters


# These scaling parameters can be used to calculate weights for elements when creating a portfolio.
#
# For example, if we have a pair portfolio of ('A', 'AA'), we can construct series of their normalized prices as:


# Normalizing the price series on our own (already done inside the DistanceStrategy class)
A_series_scaled = (train_data['A'] - scaling_parameters['min_value']['A']) / \
                  (scaling_parameters['max_value']['A'] - scaling_parameters['min_value']['A'])

AA_series_scaled = (train_data['AA'] - scaling_parameters['min_value']['AA']) / \
                   (scaling_parameters['max_value']['AA'] - scaling_parameters['min_value']['AA'])


# Plotting the results
plt.figure(figsize=(12,5))

ax1 = A_series_scaled.plot(color='blue', label='A normalized series')
ax2 = AA_series_scaled.plot(color='red', label='AA normalized series')

plt.legend()
plt.show()


# Looking at top closest pairs 
pairs


# These pairs will be used during the trading signal generation stage.


# Looking at historical standard deviations of pair portfolios
historical_std


# Generally, we can observe that with the increase of Euclidean distance between pairs the volatility is also rising.


# ### Generating trading signals


# Now let's generate trading signals for the testing dataset.


# Performing the signal generation stage using (2 * st. variation) as a threshold
strategy.trade_pairs(test_data, divergence=2)

# Getting series of portfolio values, trading signals, and normalized price series of elements for each chosen pair
portfolio_series = strategy.get_portfolios()
trading_signals = strategy.get_signals()
normalized_prices = strategy.normalized_data


# Looking at calculated portfolio value series
portfolio_series.head()


# Looking at generated trading signals - target quantities of portfolios to hold
trading_signals.head()


# Also normalized price series for each asset
normalized_prices.head()


# The DistanceStrategy class also allows plotting data for a chosen pair. Looking again at the list of chosen pairs to pick a pair to plot.


# Looking at top closest pairs 
pairs


# Let's look at normalized prices, portfolio values and generated trading signals for the pair ('BAC', 'C') - with number 7 (counting from zero).


# Plotting normalized price series of elements in a pair
figure_pair = strategy.plot_pair(7)


# Plotting portfolio value series
figure_portfolio = strategy.plot_portfolio(7)


# This pair of stocks is moving similarly over the testing period. A signal to open a sell position on a portfolio is generated in the middle of January 2019 and a signal to close this position is generated around the end of May 2019.
#
# As the long asset in a portfolio is 'BAC' and the short asset is 'C', the signal to sell a portfolio means we should sell 'BAC' and buy 'C'.
#
# We can either buy and sell one share for each asset in a pair or calculate weights for 'BAC' and 'C' based on starting prices and scaling parameters.
#
# First, we should scale by starting prices of each stock and next by scaling parameters ($max(P) - min(P)$) (returns are proportional to initial prices of stocks and negatively proportional to the scaling parameter):
#
# - $Scale_{1} = \frac{P_{1}^{0}}{P_{1}^{0} + P_{2}^{0}} * \frac{(max(P_{2}) - min(P_{2})}{(max(P_{1}) - min(P_{1})) + (max(P_{2}) - min(P_{2}))}$
#
# - $Scale_{2} = \frac{P_{2}^{0}}{P_{1}^{0} + P_{2}^{0}} * \frac{(max(P_{1}) - min(P_{1})}{(max(P_{1}) - min(P_{1})) + (max(P_{2}) - min(P_{2}))}$


# Looking at the scaling parameters (min and max values) used for elements in a portfolio
pair_scales = scaling_parameters.loc[['BAC', 'C']]

pair_scales


# So the scaling parameters for 'BAC' and 'C' are
maxmin_BAC = pair_scales.loc['BAC'][1] - pair_scales.loc['BAC'][0]
maxmin_C = pair_scales.loc['C'][1] - pair_scales.loc['C'][0]

scale_BAC = (test_data['BAC'][0] / (test_data['BAC'][0] + test_data['C'][0])) * (maxmin_C / (maxmin_BAC + maxmin_C))
scale_C = (test_data['C'][0] / (test_data['BAC'][0] + test_data['C'][0])) * (maxmin_BAC / (maxmin_BAC + maxmin_C))

print('Scaling parameter for BAC is ', scale_BAC)
print('Scaling parameter for C is ', scale_C)


# Now, let's check how much profit would this distance strategy generate on a given (BAC', 'C') pair.


# Returns of elemrnts in a test dataset
test_data_returns = (test_data / test_data.shift(1) - 1)[1:]

test_data_returns.head()


# For unscaled portfolio we'll invest 50% into the 'BAC' asset and 50% in the 'C' asset. 
#
# For scaled portfolio we should calculate the weights - make scales for 'BAC' and 'C' sum up to 1.


weight_BAC = scale_BAC / (scale_BAC + scale_C)
weight_C = 1 - weight_BAC

print("For scaled portfolio we'll invest ", round(weight_BAC, 3), "% into the BAC asset.")
print("And ", round(weight_C, 3), "% into the C asset.")


# Let's test that weight parameters are calculated right


# Pair portfolio price from returns using weight parameters
pair_portfolio_returns = test_data_returns['BAC'] * weight_BAC - test_data_returns['C'] * weight_C
pair_portfolio_price = (pair_portfolio_returns + 1).cumprod()
pair_portfolio_price.plot(title="Portfolio values for pair ('BAC', 'C') calcualted from returns based on weights", figsize=(10,5));


# As we can see, this price performance matches the pair portfolio price performance from the DistanceStrategy class plot_portfolio() function. 


# Invested portfolio prices for scaled and unscaled weights
portfolio_returns_unscaled = test_data_returns['BAC'] * 0.5 - test_data_returns['C'] * 0.5
portfolio_returns_unscaled = portfolio_returns_unscaled * (trading_signals["('BAC', 'C')"].shift(1))
portfolio_price_unscaled = (portfolio_returns_unscaled + 1).cumprod()

portfolio_returns_scaled = test_data_returns['BAC'] * weight_BAC - test_data_returns['C'] * weight_C
portfolio_returns_scaled = portfolio_returns_scaled * (trading_signals["('BAC', 'C')"].shift(1))
portfolio_price_scaled = (portfolio_returns_scaled + 1).cumprod()


# Equity curve of our unscaled portfolio price
equity_curve_unscaled = portfolio_price_unscaled - 1

equity_curve_unscaled.plot(title='Distance Strategy investemnt portfolio equity curve - unscaled weights', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_price_unscaled[-1])


# Equity curve of our scaled portfolio price
equity_curve_scaled = portfolio_price_scaled - 1

equity_curve_scaled.plot(title='Distance Strategy investemnt portfolio equity curve - scaled weights', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_price_scaled[-1])


# So using trading signals from the Distance Strategy for this particular example resulted in the equity curve of our investment portfolio increasing from 1 in mid-January 2019 to around 1.0475 in late May 2019 for the scaled portfolio and 1.0466 for the unscaled one.


# ## Conclusion


# This notebook describes the Distance Strategy class and its functionality. Also, it shows how the stages of the method (pairs formation and trading signals generation) can be used on real data and that this method can output profitable trading signals.
#
# The algorithms and the descriptions used in this notebook were described by _Gatev, E., Goetzmann, W. N.,_ and _Rouwenhorst, K. G._ in the paper __Pairs Trading: Performance of a Relative Value Arbitrage Rule__  [available here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=141615).
#
# Key takeaways from the notebook:
# - The distance approach can be divided into two stages - pairs formation and trading signals generation.
# - The distance approach works as follows:
#   - First, a historical period is defined, cumulative returns for assets in this period are normalized.
#   - Second, using the Euclidean squared distance on the normalized price time series, $n$ closest pairs of assets are picked.
#   - During the treading period, the trading signals are generated. The mechanism behind this process is the following:
#   - If the difference between the price of elements in a pair diverged by
#     more than 2 standard deviations (calculated for each pair during the training period), the positions are
#     opened - long for the element with a lower price in a portfolio and short for an element with a higher price
#     in a portfolio.
#   - These positions are closed when the normalized prices cross or when the trading period ends.
# - No cointegration tests are being performed in the distance approach, so dependencies found using this approach can be spurious.

