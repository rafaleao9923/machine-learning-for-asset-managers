# Generated from: basic_distance_approach_comparsion.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Basic Distance Approach Comparison


# This notebook aims to give a comprehensive comparison of different pairs selection methods described in our previous notebook for the basic distance approach. As in the work by Do and Faff (2010), we’ll make a portfolio for the top 20 pairs of each selection method. All selection methods are as below:
#
# 1. **Basic Strategy**: By calculating the Euclidean square distance for each of the pairs, the $n$ closest pairs are selected.
#
#
# 2. **Industry Strategy**: By calculating the Euclidean square distance for each of the pairs within the same industry group, the $n$ closest pairs are selected.
#
#
# 3. **Zero-crossings Strategy**: By sorting the pairs based on the number of spread zero crossings in the formation period, the top $n$ pairs by number of zero crossings are selected.
#
#
# 4. **Variance Strategy**: By sorting the pairs based on their historical standard deviation in the formation period, the top $n$ pairs with higher standard deviation are selected.
#
#
# 5. **Cointegration Strategy**: By conducting a cointegration test, we can pick the pairs from the basic strategy that are actually cointegrated, out of them we can pick the top $n$ pairs with the smallest p-values are selected.


# # Introduction


# We’ll use ArbitrageLab’s Basic Distance Approach module to show comparisons in this notebook. Therefore, we highly recommend seeing [here](https://hudson-and-thames-arbitragelab.readthedocs-hosted.com/en/latest/distance_approach/distance_approach.html) for more details of the module.
#
# This notebook goes as follows:
# - First, we load data and modules we need for comparisons. One may use different sources of data if the data structure is the same as in the given example.
# - Second, by using the 5 different pairs selection methods, we’ll create 5 different strategies.
# - After pairs are selected, the empirical test is conducted using test data to see which strategy performs better in a given period. 


# # Implementation


import itertools
import arbitragelab as al
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts 


# ## Loading Data


# As we did in the Basic Distance Approach research notebook(basic_distance_appraoch.ipynb), we'll download price time series for 272 stocks over a period from 01.2018 to 07.2019. First 12 months of data will be used for training and the following 6 months for trading signal generation and analysis of results. 
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


# ## Pair Selection Methods


# To learn the details of each of the pairs selection methods, please refer to our [documentation](https://hudson-and-thames-arbitragelab.readthedocs-hosted.com/en/latest/distance_approach/distance_approach.html). 
#
# As mentioned above, we’ll select the top 15 pairs for each strategy. However, for the cointegration strategy, we’ll select the top 50 pairs first and test the cointegrating relationship between pairs so that we can pick the pairs taht are actually cointegrated. 


# Defining three different pair selection criteria 
strategy_basic = al.distance_approach.DistanceStrategy()
strategy_industry = al.distance_approach.DistanceStrategy()
strategy_zero_crossing = al.distance_approach.DistanceStrategy()
strategy_variance = al.distance_approach.DistanceStrategy()
strategy_coint = al.distance_approach.DistanceStrategy()

# Performing the pairs formation step and picking top 15 pairs
strategy_basic.form_pairs(train_data, num_top=15)
strategy_industry.form_pairs(train_data, industry_dict=industry_dict, 
                             num_top=15)
strategy_zero_crossing.form_pairs(train_data, method='zero_crossing', 
                             industry_dict=industry_dict, num_top=15)
strategy_variance.form_pairs(train_data, method='variance',
                             industry_dict=industry_dict, num_top=15)
strategy_coint.form_pairs(train_data, industry_dict=industry_dict, 
                          num_top=50)


# Here, by using a module from [statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.coint.html), the Null hypothesis is that there is no cointegration, the alternative hypothesis is that there is a cointegrating relationship. If the p-value is small, below a critical size, then we can reject the hypothesis that there is no cointegrating relationship.
#
# Below is a simple function returning a list containing tuples of two strings that are cointegrated. One may use the function to test the cointegration of the pairs. There is also a cointegration module in our ArbitrageLab so we highly recommend reading [here](https://hudson-and-thames-arbitragelab.readthedocs-hosted.com/en/latest/cointegration_approach/cointegration_tests.html) and utilizing it as well.


def get_coint_pairs(pairs, train_data, critical_val=0.05):
    """
    Selects pairs which are cointegrated at the given critical values only.

    For cointegration test, Engle-Granger two-step cointegration test is used.

    :param pairs: (list) List containing tuples of two strings, for names of elements in a pair.
    :param train_data: (pd.DataFrame) Dataframe with training data used to create asset pairs.
    :param critical_val: (float) Critical value to reject the null hypothesis. By default, it's 0.05.
    :return: (list) List containing tuples of two strings that are cointegrated.
    """

    # Make an empty dictionary for cointegrated pairs
    pairs_coint = {}

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
            pairs_coint[pair] = p_value

    return pairs_coint


# If we get more than 15 pairs after the cointegrations testing, we will pick the top ones based on the p-values.


# Get pairs and scaling parameter for cointegration strategy
pairs_coint = strategy_coint.get_pairs()
scaling_coint = strategy_coint.get_scaling_parameters()

# Get a dictionary of pairs and p-value after the cointegration test
pairs_coint = get_coint_pairs(pairs_coint, train_data)

# Sort a dictionary by its item values
pairs_coint = dict(sorted(pairs_coint.items(), key=lambda item: item[1]))

# Get only top 15 pairs from the dictionary
num_top = 15
pairs_coint = list(dict(itertools.islice(pairs_coint.items(), num_top)).keys())

# Assign the selected pairs as the strategy's pairs
strategy_coint.pairs = pairs_coint


# We’ll just use the `get_pairs()` method for other strategies to get the top 15 pairs.


# Getting a list of created pairs for each of the strategy
pairs_basic = strategy_basic.get_pairs()
pairs_industry = strategy_industry.get_pairs()
pairs_zero_crossing = strategy_zero_crossing.get_pairs()
pairs_variance = strategy_variance.get_pairs()


# Let’s see all the pairs selected by each method. We’ll see the profitability of each pair in the table below after testing all the strategies.


# Showing pairs selected by each method
pair_dataframe = pd.DataFrame([pd.Series(pairs_basic), pd.Series(pairs_industry),pd.Series(pairs_zero_crossing), 
                               pd.Series(pairs_variance),pd.Series(pairs_coint)],
                              index =['Basic','Industry','Zero-Crossing','Variance','Cointegration']).T

display(pair_dataframe)


# ## Testing strategies


# Now we’ll test each of the strategies by forming an equally weighted portfolio with the selected pairs. 
#
# Here, we follow the trading rule by Do and Faff (2010). If the portfolio value exceeds two historical deviations, a sell signal is generated - we expect the price of the first element to decrease and the price of the second element to increase. And if the value of the portfolio is below minus two historical deviations, a buy signal is generated.
#
# An open position is closed when the portfolio value crosses the zero mark - or when the prices of elements in a pair cross. So at any given time, we have one (buy or sell) or none active positions opened. This makes cost allocation for the strategy easier. The resulting trading signals are target quantities of portfolios to hold for each pair (with values -1, 0, or +1).
#
# In the get_portfoio_return function below, we generate these signals and trade based on these for every portfolio. Then we average the returns of the portfolios by equal weight for simple comparison. 


def get_portfolio_return(strategy, test_data):
    """
    Ouputs a series of portfolio returns for a given strategy.

    :params strategy: (Class) DistanceStratgey Class with pairs formed with form_pair().
    :params test_data: (pd.DataFrame) Dataframe with testing data used to create trading signals.
    :return: (pd.Series) Series of portfolio returns in the test period.
    """

    # Getting a list of created pairs for each chosen pair portfolio
    pairs = strategy.get_pairs()

    # Performing the signal generation stage using (2 * st. variation) as a threshold
    strategy.trade_pairs(test_data, divergence=2)

    # Getting series of portfolio values, trading signals, and normalized price series of elements for each chosen pair
    index_columns = [str(pair) for pair in pairs]
    portfolio_series = strategy.get_portfolios()
    portfolio_series = portfolio_series.loc[:,portfolio_series.columns.isin(index_columns)]
    trading_signals = strategy.get_signals()
    trading_signals = trading_signals.loc[:,trading_signals.columns.isin(index_columns)]

    # Returns of elemrnts in a test dataset
    test_data_returns = (test_data / test_data.shift(1) - 1)[1:]

    # Making empty dataframe and list for storing returns of the pairs
    total_return = pd.Series([], dtype='float64')
    pair_return = []
    
    for pair in pairs:
        first_stock, second_stock = pair
        portfolio_returns_scaled = test_data_returns[first_stock] * 0.5 - test_data_returns[second_stock] * 0.5
        portfolio_returns_scaled = portfolio_returns_scaled * (trading_signals[str(pair)].shift(1))
        portfolio_price_scaled = (portfolio_returns_scaled + 1).cumprod()

        # Equity curve of our scaled portfolio price
        equity_curve_scaled = portfolio_price_scaled - 1
        
        # Appends the return of the pair into the list and total return into the dataframe
        pair_return.append(equity_curve_scaled[-1])
        total_return = total_return.add(equity_curve_scaled, fill_value=0)
    
    # Reformatting the returns of the pairs for better visualization later
    pair_return = [ '%.4f' % value for value in pair_return ]
    
    # Calculates the average return of the portfolio
    total_return = total_return/len(pairs)
    
    return pair_return, total_return


# Below are the results of the test for every portfolio. 


# Get portfolio return for basic strategy
pair_return_basic, portfolio_basic = get_portfolio_return(strategy_basic, test_data)

# Plot the equity curve and print the excess return of the portfolio
portfolio_basic.plot(title='Distance Strategy investment portfolio equity curve - Basic Strategy', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_basic[-1])


# Get portfolio return for industry strategy
pair_return_industry, portfolio_industry = get_portfolio_return(strategy_industry, test_data)

# Plot the equity curve and print the excess return of the portfolio
portfolio_industry.plot(title='Distance Strategy investment portfolio equity curve - Industry Strategy', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_industry[-1])


# Get portfolio return for variance strategy
pair_return_zero_crossing, portfolio_zero_crossing = get_portfolio_return(strategy_zero_crossing, test_data)

# Plot the equity curve and print the excess return of the portfolio
portfolio_zero_crossing.plot(title='Distance Strategy investment portfolio equity curve - Zero-Crossing Strategy',
                             figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_zero_crossing[-1])


# Get portfolio return for variance strategy
pair_return_variance, portfolio_variance = get_portfolio_return(strategy_variance, test_data)

# Plot the equity curve and print the excess return of the portfolio
portfolio_variance.plot(title='Distance Strategy investment portfolio equity curve - Variance Strategy', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_variance[-1])


# Get portfolio return for cointegration strategy
pair_return_coint, portfolio_coint = get_portfolio_return(strategy_coint, test_data)

# Plot the equity curve and print the excess return of the portfolio
portfolio_coint.plot(title='Distance Strategy investment portfolio equity curve - Cointegration Strategy', figsize=(10,5));
print('Investment portfolio value rose to ', portfolio_coint[-1])


# Before we wrap up, one may look into the details of portfolio returns for each pair as below. One thing to note is that although the variance method has the highest portfolio return among the five methods, it has two pairs with zero returns implying that these pairs are not traded at all during the test period. As it might not be the most desirable result we want from pairs trading, some other combinations of methods could be tried using this module. 


# Showing pairs selected by each method and its returns
pair_returns = pd.DataFrame([pairs_basic, pair_return_basic,pairs_industry, pair_return_industry,
                pairs_zero_crossing, pair_return_zero_crossing,pairs_variance,pair_return_variance,
                pairs_coint, pair_return_coint]).T
columns = ['Basic','Return' ,'Industry','Returns','Zero-Crossing','Returns','Variance','Returns','Cointegration','Returns']
pair_returns.columns = columns
display(pair_returns)


# # Conclusion


# Among the 5 different strategies, the variance method performs better than the others in the test period. Analyzing the plots, the variance strategy portfolio shows a more steady performance in comparison to other strategies. But still, it showed a drawdown in June 2019.
#
# As this notebook conducted testing distance approach strategies for a specific period in time, this might not always be the case that the variance strategy performs the best. The proposed code examples can be used to analyze which modification would better suit a specific case, we encourage to test these strategies on different time periods and data sets.
#
# Key takeaways from the notebook:
# - As in the work by Do and Faff (2010), the basic method performs worst among 5 different strategies, which means additional pairs selection criteria might be needed other than the smallest Euclidean distance.
# - The variance method performs well as theoretically, the pairs with a higher standard deviation in the formation period assure more volatile spreads, resulting in higher profit opportunities in the testing period.
# - Conducting a cointegration test to select pairs that have a high cointegrating relationship works as the cointegration strategy performs better than the basic and industry strategy, supporting the hypothesis mentioned in the work of Krauss (2017).


# ## References ##
# - [Gatev, E., Goetzmann, W.N. and Rouwenhorst, K.G., 2006. Pairs trading: Performance of a relative-value arbitrage rule. The Review of Financial Studies, 19(3), pp.797-827.](https://www.stat.rutgers.edu/home/hxiao/fsrm588_2013/gatev.pdf)
# - [Do, B. and Faff, R., 2012. Are pairs trading profits robust to trading costs?. Journal of Financial Research, 35(2), pp.261-287.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1707125)
# - [Do, B. and Faff, R., 2010. Does simple pairs trading still work?. Financial Analysts Journal, 66(4), pp.83-95](https://www.jstor.org/stable/25741293?seq=1)
# - [Krauss, C., 2017. Statistical arbitrage pairs trading strategies: Review and outlook. Journal of Economic Surveys, 31(2), pp.513-545.](https://www.econstor.eu/bitstream/10419/116783/1/833997289.pdf)

