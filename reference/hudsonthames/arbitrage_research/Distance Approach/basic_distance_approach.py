# Generated from: basic_distance_approach.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Basic Distance Approach


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
# There are, however, possible adjustments to this strategy, like selecting pairs based on different criteria such as the number of zero crossings or historical variance, choosing distances other than the Euclidean square distance, adjusting the threshold to enter a trade for each pair, etc. 


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
# distances are then sorted in the ascending order and the $n$ closest pairs are picked (our
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


# ## Pair selection criteria
#
# As basic pairs formation confirms declining profitability in pairs trading, some other refined pair selection criteria have emerged. Here, we describe three different methods from the basic approach in selecting pairs for trading. 
#
# First is only allowing for matching securities within the same industry group. The second is sorting selected pairs based on the number of zero-crossings in the formation period and the third is sorting selected pairs based on the historical standard deviation where pairs with high standard deviation are selected.
#
# 1. **Pairs within the same industry group**
#
# In the pairs formation step above, one can add this method when finding pairs in order to match securities within the same industry group. 
#
# With a dictionary containing the name/ticker of the securities and each corresponding industry group, the securities are first separated into different industry groups. Then, by calculating the Euclidean square distance for each of the pair within the same group, the $n$ closest pairs are selected(our function also allows skipping a number of first pairs, so one can choose pairs 10-15 to study). 
#
# This pair selection criterion can be used alongside other methods such as zero-crossings or variance if one gives a dictionary of industry group as an input. This will allow sorting pairs by alternative criteria but within one industry group.
#
# 2. **Pairs with a higher number of zero-crossings**
#
# The number of zero crossings in the formation period has a positive relation to the future spread convergence according to the work by Do and Faff (2010). 
#
# After pairs were matched either within the same industry group or from different industries, the top $n$ pairs that had the highest number of zero crossings during the formation period are admitted to the portfolio we select. This method incorporates the time-series dimension of the historical data in the form of the number of zero crossings. 
#
# 3. **Pairs with a higher historical standard deviation**
#
# The historical standard deviation calculated in the formation period can also be a criterion to sort selected pairs. 
#
# After pairs were matched, we can sort them based on their historical standard deviation in the formation period. According to the work of Do and Faff(2010), as having a small SSD decreases the variance of the spread, this approach should increase the expected profitability of the method.
#
# 4. **Pairs with a cointegrating relationship(Optional)**
#
# For the pairs matched, a cointegration test can also be conducted to select pairs that have cointegrating relationships. 
#
# By using an augmented Engle-Granger two-step cointegration test with a critical value, the pairs having a lower p-value than the critical value are selected. These pairs are expected to have better performance during the trading period, as proposed in the work by Krauss (2017).


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
# - **get_num_crossing()** outputs a list of tuples, containing chosen top pairs with its number of zero-crossings.
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
import statsmodels.tsa.stattools as ts 


# ### Loading data


# As a dataset, we'll download the price time series for 272 stocks over a period from 01.2018 to 07.2019. First 12 months of data will be used for training and the following 6 months for trading signal generation and analysis of results. 
#
# Also, for industry-group based selection, we’ll use 4 major industries in S&P 500 stocks: Information Technology, Industrials, Financials and Healthcare. We’ll download this data from [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) but any source of data can be used if we follow the dictionary style as below.


# Get industry data from Wikipedia 
table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
stock_table = table[0]

# Indutry groups to use are below
industry_group = ['Information Technology','Industrials','Financials',
                  'Health Care']

# Get tickers from S&P 500 which are in those industry groups
ticker_industry = stock_table[stock_table['GICS Sector']
                              .isin(industry_group)].reset_index(drop=True)

# Get a dataframe of ticker and industry group
ticker_industry = ticker_industry[['Symbol','GICS Sector']]

# Get tickers to use as a list
tickers = ticker_industry['Symbol'].to_list()
remove_tickers = ['CARR','ABC','BRK.B','VNT','OTIS'] # Removed tickers
tickers = [ticker for ticker in tickers if ticker not in remove_tickers]

# Get a dictionary of industry group
industry_dict = pd.Series(ticker_industry['GICS Sector'].values,
                          index=ticker_industry['Symbol']).to_dict()

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


# Looking at top closest pairs 
pairs


# For example, if we have a pair portfolio of ('MSFT', 'V'), we can construct series of their normalized prices as:


# Normalizing the price series on our own (already done inside the DistanceStrategy class)
MSFT_series_scaled = (train_data['MSFT'] - scaling_parameters['min_value']['MSFT']) / \
                  (scaling_parameters['max_value']['MSFT'] - scaling_parameters['min_value']['MSFT'])

V_series_scaled = (train_data['V'] - scaling_parameters['min_value']['V']) / \
                   (scaling_parameters['max_value']['V'] - scaling_parameters['min_value']['V'])


# Plotting the results
plt.figure(figsize=(12,5))

ax1 = MSFT_series_scaled.plot(color='blue', label='MSFT normalized series')
ax2 = V_series_scaled.plot(color='red', label='V normalized series')

plt.legend()
plt.show()


# Looking at top closest pairs 
pairs


# These pairs will be used during the trading signal generation stage.


# Looking at historical standard deviations of pair portfolios
historical_std


# Generally, we can observe that with the increase of Euclidean distance between pairs the volatility is also rising.


# ### Alternative pair selection methods


# As basic pairs formation confirms declining profitability in pairs trading, some other refined pair selection criteria have emerged. Here, we describe three different methods from the basic approach in selecting pairs for trading.
#
# First is only allowing for matching securities within the same industry group. The second is sorting selected pairs based on the number of zero-crossings in the formation period and the third is sorting selected pairs based on the historical standard deviation where pairs with high standard deviation are selected.


# Now let’s make strategies for each of the selection method. 


# Defining three different pair selection criteria 
strategy_industry = al.distance_approach.DistanceStrategy()
strategy_zero_crossing = al.distance_approach.DistanceStrategy()
strategy_variance = al.distance_approach.DistanceStrategy()

# Performing the pairs formation step and picking top 20 pairs
strategy_industry.form_pairs(train_data, industry_dict=industry_dict, 
                             num_top=20)
strategy_zero_crossing.form_pairs(train_data, method='zero_crossing', 
                             industry_dict=industry_dict, num_top=20)
strategy_variance.form_pairs(train_data, method='variance',
                             industry_dict=industry_dict, num_top=20)

# Getting a list of created pairs for each of the strategy
pairs_industry = strategy_industry.get_pairs()
pairs_zero_crossing = strategy_zero_crossing.get_pairs()
pairs_variance = strategy_variance.get_pairs()

# Getting scaling values used to normalize data
scaling_industry = strategy_industry.get_scaling_parameters()
scaling_zero_crossing = strategy_zero_crossing.get_scaling_parameters()
scaling_variance = strategy_variance.get_scaling_parameters()


# **(Optional) Cointegration Test**
#
# For the pairs selected, we’ll conduct a cointegration test to see which pairs are actually cointegrated, as these pairs may perform better during the trading period. We’ll use the augmented Engle-Granger two-step cointegration test here and as the results of the test only belong to the data we selected, one may perform different tests on different datasets.
#
# A brief introduction to Engle-Granger two-step cointegration test method is in below.
#
# For two stocks in a pair, let’s say stock 1 and stock 2, as we do not know $\beta$, we estimate it by using ordinary least squares, and then run the stationarity test on the estimated $u_{t}$ series. 
#
# $$stock1_{t}-\beta stock2_{t}=u_{t}$$
#
# Here, by using a module from [statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.coint.html), the Null hypothesis is that there is no cointegration, the alternative hypothesis is that there is cointegrating relationship. If the p-value is small, below a critical size, then we can reject the hypothesis that there is no cointegrating relationship.


# Below is a simple function returning a list containing tuples of two strings that are cointegrated. One may use the function to test the cointegration of the pairs. There is also a cointegration module in our Arbitrage Lab so we highly recommend reading [here](https://hudson-and-thames-arbitragelab.readthedocs-hosted.com/en/latest/cointegration_approach/cointegration_tests.html) and utilize it as well.


def get_coint_pairs(pairs, train_data, critical_val = 0.05):
    """
    Selects pairs which are cointegrated at the given critical values only.

    For cointegration test, Engle-Granger two-step cointegration test is used.

    :param pairs: (list) List containing tuples of two strings, for names of elements in a pair.
    :param train_data: (pd.DataFrame) Dataframe with training data used to create asset pairs.
    :param critical_val: (float) Critical value to reject the null hypothesis. By default, it's 0.05.
    :return: (list) List containing tuples of two strings that are cointegrated.
    """

    # Make an empty list for cointegrated pairs
    pairs_coint = []

    # Perform hypothesis test for every pair in the pairs list
    for pair in pairs:

        # Select each stock in the pair
        first_ticker = pair[0]
        second_ticker = pair[1]

        # Get data for each of the stock with scaling parameter
        first_stock = train_data[first_ticker].fillna(method='ffill')

        second_stock = train_data[second_ticker].fillna(method='ffill')

        # Conduct a cointegration test and get p-value
        p_value = ts.coint(first_stock.values, second_stock.values)[1]

        # Check whether the p-value is below the critical value and add to a list if it is.
        if p_value < critical_val:
            pairs_coint.append(pair)

    return pairs_coint


# Pairs that have a cointegrating relationship in standard strategy.


get_coint_pairs(pairs, train_data)


# Pairs that have a cointegrating relationship within the same industry.


get_coint_pairs(pairs_industry, train_data)


# ### Generating trading signals


# Now let's generate trading signals for the testing dataset.
#
# We are testing the standard strategy here but strategies using other methods can also be used if one changes the original strategy to other strategies in the codes below.


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


# Let's look at normalized prices, portfolio values and generated trading signals for the pair ('CMA', 'RF') - with number 4 (counting from zero).


# Plotting normalized price series of elements in a pair
figure_pair = strategy.plot_pair(4)


# Plotting portfolio value series
figure_portfolio = strategy.plot_portfolio(4)


# This pair of stocks is moving similarly over the testing period. A signal to open a sell position on a portfolio is generated in the middle of February 2019 and a signal to close this position is generated around April of 2019.
#
# As the long asset in a portfolio is 'CMA' and the short asset is 'RF', the signal to sell a portfolio means we should sell 'CMA' and buy 'RF'.
#
# We can either buy and sell one share for each asset in a pair or calculate weights for 'CMA' and 'RF' based on starting prices and scaling parameters.
#
# First, we should scale by starting prices of each stock and next by scaling parameters ($max(P) - min(P)$) (returns are proportional to initial prices of stocks and negatively proportional to the scaling parameter):
#
# - $Scale_{1} = \frac{P_{1}^{0}}{P_{1}^{0} + P_{2}^{0}} * \frac{(max(P_{2}) - min(P_{2})}{(max(P_{1}) - min(P_{1})) + (max(P_{2}) - min(P_{2}))}$
#
# - $Scale_{2} = \frac{P_{2}^{0}}{P_{1}^{0} + P_{2}^{0}} * \frac{(max(P_{1}) - min(P_{1})}{(max(P_{1}) - min(P_{1})) + (max(P_{2}) - min(P_{2}))}$


# Looking at the scaling parameters (min and max values) used for elements in a portfolio
pair_scales = scaling_parameters.loc[['CMA', 'RF']]

pair_scales


# So the scaling parameters for 'CMA' and 'RF' are
maxmin_CMA = pair_scales.loc['CMA'][1] - pair_scales.loc['CMA'][0]
maxmin_RF = pair_scales.loc['RF'][1] - pair_scales.loc['RF'][0]

scale_CMA = (test_data['CMA'][0] / (test_data['CMA'][0] + test_data['RF'][0])) * (maxmin_RF / (maxmin_CMA + maxmin_RF))
scale_RF = (test_data['RF'][0] / (test_data['CMA'][0] + test_data['RF'][0])) * (maxmin_CMA / (maxmin_CMA + maxmin_RF))

print('Scaling parameter for CMA is ', scale_CMA)
print('Scaling parameter for RF is ', scale_RF)


# Now, let's check how much profit would this distance strategy generate on a given ('CMA', 'RF') pair.


# Returns of elemrnts in a test dataset
test_data_returns = (test_data / test_data.shift(1) - 1)[1:]

test_data_returns.head()


# For unscaled portfolio we'll invest 50% into the 'CMA' asset and 50% in the 'RF' asset. 
#
# For scaled portfolio we should calculate the weights - make scales for 'CMA' and 'RF' sum up to 1.


weight_CMA = scale_CMA / (scale_CMA + scale_RF)
weight_RF = 1 - weight_CMA

print("For scaled portfolio we'll invest ", round(weight_CMA, 3), "% into the CMA asset.")
print("And ", round(weight_RF, 3), "% into the RF asset.")


# Let's test that weight parameters are calculated right


# Pair portfolio price from returns using weight parameters
pair_portfolio_returns = test_data_returns['CMA'] * weight_CMA - test_data_returns['RF'] * weight_RF
pair_portfolio_price = (pair_portfolio_returns + 1).cumprod()
pair_portfolio_price.plot(title="Portfolio values for pair ('CMA', 'RF') calcualted from returns based on weights", figsize=(10,5));


# As we can see, this price performance matches the pair portfolio price performance from the DistanceStrategy class plot_portfolio() function. 


# Invested portfolio prices for scaled and unscaled weights
portfolio_returns_unscaled = test_data_returns['CMA'] * 0.5 - test_data_returns['RF'] * 0.5
portfolio_returns_unscaled = portfolio_returns_unscaled * (trading_signals["('CMA', 'RF')"].shift(1))
portfolio_price_unscaled = (portfolio_returns_unscaled + 1).cumprod()

portfolio_returns_scaled = test_data_returns['CMA'] * weight_CMA - test_data_returns['RF'] * weight_RF
portfolio_returns_scaled = portfolio_returns_scaled * (trading_signals["('CMA', 'RF')"].shift(1))
portfolio_price_scaled = (portfolio_returns_scaled + 1).cumprod()


# Equity curve of our unscaled portfolio price
equity_curve_unscaled = portfolio_price_unscaled - 1

equity_curve_unscaled.plot(title='Distance Strategy investemnt portfolio equity curve - unscaled weights', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_price_unscaled[-1])


# Equity curve of our scaled portfolio price
equity_curve_scaled = portfolio_price_scaled - 1

equity_curve_scaled.plot(title='Distance Strategy investemnt portfolio equity curve - scaled weights', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_price_scaled[-1])


# So using trading signals from the Distance Strategy for this particular example resulted in the equity curve of our investment portfolio increasing from 1 in mid-January 2019 to around 1.0357 in late May 2019 for the scaled portfolio and 1.0352 for the unscaled one.


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
# - Other refined pair selection criteria have emerged:
#   - First is only allowing for matching securities within the same industry group.
#   - The second is sorting selected pairs based on the number of zero-crossings in the formation period.
#   - The third is sorting selected pairs based on the historical standard deviation where pairs with high standard deviation     are selected.
# - No cointegration tests are being performed in the distance approach by default, so dependencies found using this approach can be spurious.
# - We show how a cointegration test can also be conducted to select pairs that have cointegrating relationships. These pairs are expected to have better performance during the trading period.


# ## References ##
# - [Gatev, E., Goetzmann, W.N. and Rouwenhorst, K.G., 2006. Pairs trading: Performance of a relative-value arbitrage rule. The Review of Financial Studies, 19(3), pp.797-827.](https://www.stat.rutgers.edu/home/hxiao/fsrm588_2013/gatev.pdf)
# - [Do, B. and Faff, R., 2012. Are pairs trading profits robust to trading costs?. Journal of Financial Research, 35(2), pp.261-287.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1707125)
# - [Do, B. and Faff, R., 2010. Does simple pairs trading still work?. Financial Analysts Journal, 66(4), pp.83-95](https://www.jstor.org/stable/25741293?seq=1)
# - [Krauss, C., 2017. Statistical arbitrage pairs trading strategies: Review and outlook. Journal of Economic Surveys, 31(2), pp.513-545.](https://www.econstor.eu/bitstream/10419/116783/1/833997289.pdf)

