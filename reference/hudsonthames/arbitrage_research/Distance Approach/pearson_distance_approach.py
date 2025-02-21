# Generated from: pearson_distance_approach.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Pearson Approach


# This description of the distance approach closely follows the paper by _Chen et al._ __Empirical investigation of an equity pairs trading strategy__  [available here](http://www.pbcsf.tsinghua.edu.cn/research/chenzhuo/paper/Empirical%20Investigation%20of%20an%20Equity%20Pairs%20Trading%20Strategy.pdf). 


# ## Introduction


# After the distance approach was introduced in the paper by Gatev et al. (2006), a lot of research has been
# conducted to further develop the original distance approach. One of the adjustments is the Pearson correlation
# approach proposed by Chen et al.(2012). In this paper, the authors use the same data set and time frame as
# in the work by Gatev et al.(2006) but they used Pearson correlation on return level for forming pairs.
# In the formation period(5 years in the paper), pairwise return correlations for all pairs in the universe
# are calculated based on monthly return data. Then the authors construct a new variable, Return Divergence
# ($D_{i j t}$), to capture the return divergence between a single stock’s return and its pairs-portfolio returns:
#
#
# $$D_{i j t}=\beta\left(R_{i t}-R_{f}\right)-\left(R_{j t}-R_{f}\right)$$
#
#
# where $\beta$ denotes the regression coefficient of stock's monthly return $R_{i t}$ on its
# pairs-portfolio return $R_{j t}$, and $R_{f}$ is the risk-free rate
#
# The hypothesis in this approach is that if a stock’s return deviates from its pairs portfolio returns more
# than usual, this divergence is expected to be reversed in the next month. And the returns of this stock are
# expected to be abnormally high/low in comparison to other stocks.
#
# Therefore, after calculating the return divergence of all the stocks,  a long-short portfolio is constructed
# based on the long and short ratio given by the user.


# ## Pairs portfolio formation step
#
#
# This stage of PearsonStrategy consists of the following steps:
#
# 1. **Data preprocessing**
#
# As the method has to compute all of the pairs’ correlation values in the following steps, for $m$ stocks,
# there are $\frac{m*(m-1)}{2}$ correlations to be computed in the formation period. As the number of
# observations for the correlations grows exponentially with the number of stocks, this estimation is
# computationally intensive.
#
# Therefore, to reduce the computation burden, this method uses monthly stock returns data in the formation
# period (ex. 60 monthly stock returns if the formation period is 5 years). If the daily price data is given,
# the method calculates the monthly returns before moving into the next steps.
#
# 2. **Finding pairs**
#
# For each stock, the method finds $n$ stocks with the highest correlations to the stock as its pairs using
# monthly stock returns. After pairs are formed, returns of pairs, which refer to as pairs portfolios in the paper,
# are needed to create $beta$ in the following step. Therefore, this method uses two different weighting
# metrics in calculating the returns.
#
#
# The first is an equal-weighted portfolio. The method by default computes the pairs portfolio returns as the
# equal-weighted average returns of the top n pairs of stocks. The second is a correlation-weighted portfolio.
# If this metric is chosen, the method uses the stock’s correlation values to each of the pairs and forms a
# portfolio weighted by these values and the weights are calculated by the formula:
#
#
#
# $$w_{k}=\frac{\rho_{k}}{\sum_{i=1}^{n} \rho_{i}}$$
#
# where $w_{k}$ is the weight of stock k in the portfolio and $\rho_{i}$ is a correlation of the stock
# and one of its pairs.
#
# 3. **Calculating beta**
#
# After pairs portfolio returns are calculated, the method derives beta from the monthly return of the stock and
# its pairs portfolio. By using linear regression, setting stock return as independent variable and pairs portfolio
# return as the dependent variable, the methods set beta as a regression coefficient. Then the beta is stored in a
# dictionary for future uses in trading. 


# ## Trading signals generation
#
#
# After calculating the betas for all of the stocks in the formation period, the next step is to generate trading
# signals by calculating the return divergence for each of the stocks. In this method, test data is not necessarily
# required if only a trading signal for the last month of formation period is needed. However, if one wants to
# see the backtesting results of the method and test with test data, a successive dataset after the formation period
# is required to generate the proper trading signals. The steps are as follows:
#
# 1. **Data Preprocessing**
#
# The same data preprocessing is done with the formation period as the data needs to be in the same format. As in
# the formation period, risk free rate can be given in the form of either a float number of a series of data.
#
# 2. **Calculating the Return Divergence**
#
# For every month of test data, starting from the very last month of the train data, return divergences are calculated
# with the beta created in the formation period. The equation for calculating the return divergence is in the first section
# of this documentation. Note that while the return divergence between a portfolio of $n$ most-highly correlated stocks
# with stock i and stock $i$ is used as a sorting variable, only individual stock $i$ enters the portfolio
# construction, not those $n$ stocks. The portfolio of those $n$ stocks only serves as a benchmark for portfolio sorting.
#
# 3. **Finding Trading Signals**
#
# Then, all stocks are sorted in descending order based on their previous month's return divergence.  If the percentages
# of long and short stocks are given, say $p\%$ and $q\%$, the top $p\%$ of the sorted stocks are chosen
# for the long stocks and the bottom $q\%$ of the sorted stocks are chosen for the short stocks. If a user wants to
# construct a dollar-neutral portfolio, one should choose the same percentage for $p$ and $q$. Finally,
# a new dataframe is created with all of the trading signals: 1 if a stock is in a long position, -1 if it is in a short
# position and 0 if it does not have any position.


# ## Results output 
# The PearsonStrategy class contains multiple methods to get results in the desired form.
#
# Functions that can be used to get data:
#
# - **get_trading_signal()** outputs trading signal in monthly basis. 1 for a long position, -1 for a short position and 0 for closed position.
#
# - **get_beta_dict()** outputs beta, a regression coefficients for each stock, in the formation period.
#
# - **get_pairs_dict()** outputs top n pairs selected during the formation period for each of the stock.


# ## Usage of the Algorithms


# Let's use the above strategy on real data. 
#
# First, we will choose a training period of 12 months to form pairs. Second, we'll create trading signals for the following 6 months window. Finally, we will analyze the obtained results. 


import arbitragelab as al
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns


# ### Loading data


# As a dataset, we'll download the price time series for 272 stocks over a period from 01.2018 to 07.2019. First 5 years of data will be used for training and the following 1 year for trading signal generation and analysis of results. 
#
# Here, we'll use tickers from S&P 500, which are in 4 main industry groups and will use Treasury Yield 10 Years (^TNX) rate as a risk-free rate. However, any source of data can be applied the same as this.


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
remove_tickers = ['CARR','ABC','BRK.B','VNT','OTIS','OGN'] # Removed tickers
tickers = [ticker for ticker in tickers if ticker not in remove_tickers]

# Get a dictionary of industry group
industry_dict = pd.Series(ticker_industry['GICS Sector'].values,
                          index=ticker_industry['Symbol']).to_dict()

# Loading data
train_data =  yf.download(tickers, start="2015-01-02", end="2018-12-31")
test_data =  yf.download(tickers, start="2019-01-02", end="2019-12-31")

# Taking close prices for chosen instruments
train_data = train_data["Adj Close"]
test_data = test_data["Adj Close"]

# Risk free rate for train and test
risk_free_train = yf.download("^TNX", start="2015-01-02", end="2018-12-31")
risk_free_test = yf.download("^TNX", start="2019-01-02", end="2019-12-31")

# Get a series of risk free rate from the data
risk_free_train = risk_free_train['Adj Close']/100
risk_free_test = risk_free_test['Adj Close']/100

# Looking at the downloaded data
train_data.head()


# The risk free rate series should look like below.


risk_free_train.head()


# ### Forming pairs portfolios


# Now let’s form pairs portfolios and calculate beta for trading signals generation later. 


# Initialising an object containing needed methods
strategy = al.distance_approach.PearsonStrategy()

# Forming pairs portfolio with training data
strategy.form_portfolio(train_data, risk_free_train)


# Variation of the strategy can be applied by changing the number of pairs in the pairs portfolio or changing the weight metric. 


# Initialising an object containing needed methods
strategy_corr = al.distance_approach.PearsonStrategy()

# Forming pairs portfolio with training data
strategy_corr.form_portfolio(train_data, risk_free_train, num_pairs=30,
                             weight='correlation')


# For example, if we look at a pair of stocks (‘A’ and ‘TMO’), we can see that the monthly return moves very similarly to each other in the plot. 


# Get a pair for the stock 'A'
A_pairs_5 = strategy_corr.pairs_dict['A'][:1]

# Appending the stock 'A' to the list 
A_pairs_5.append('A')

# Get monthly return data for both stocks
A_pairs_return = strategy_corr.monthly_return.loc[:,A_pairs_5]

# Plot the return graph
A_pairs_return.plot(figsize=(12,8));


# Also, if we look at the beta, we can see a big difference between beta values of different stocks. Below is a figure showing two stocks with high beta (_ENPH_) and low beta (_RE_). We can clearly see that the stock with high beta has a bigger regression coefficient than the one with low beta.


# Get beta and pairs for the strategy
beta,pairs = strategy.beta_dict, strategy.pairs_dict

# Sort the beta dictionary based on the value
beta_sorted = {k: v for k, v in sorted(beta.items(), 
                                       key=lambda item: item[1])}

# Get pairs and return of ENPH and RE
ENPH_pairs, RE_pairs = pairs['ENPH'], pairs['RE']
ENPH_return = strategy.monthly_return.loc[:,'ENPH']
RE_return = strategy.monthly_return.loc[:,'RE']

# Get pairs return of both stocks
ENPH_pairs_return = strategy.monthly_return.loc[:,ENPH_pairs] 
RE_pairs_return = strategy.monthly_return.loc[:,RE_pairs] 

# Get mean return for both of the stock pairs
ENPH_pairs_mean = ENPH_pairs_return.mean(axis=1)
RE_pairs_mean = RE_pairs_return.mean(axis=1)

# Create new dataframes to store both of the stock returns
ENPH = pd.concat([ENPH_return, ENPH_pairs_mean], axis=1)
RE = pd.concat([RE_return, RE_pairs_mean], axis=1)

# Reset the columns for clarification
ENPH.columns = ['ENPH','ENPH_Pairs_Portfolio']
RE.columns = ['RE', 'RE_Pairs_Portfolio']

# Set the fig settings
fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(8,15))
fig.suptitle('Linear Regression Plot of ENPH, RE and its Pairs Portfolio')
fig.subplots_adjust(top=0.95)

# Plot two graphs
sns.regplot(ax=ax1, x="ENPH_Pairs_Portfolio", y="ENPH", data=ENPH)
ax1.set(ylim=(-0.5,0.5))

sns.regplot(ax=ax2, x="RE_Pairs_Portfolio",y="RE",data=RE);
ax2.set(ylim=(-0.5,0.5));


# ### Generating trading signals


# Now let's generate trading signals for the testing dataset.
#
# For correlation strategy, we'll adjust the long and short percentage of stocks in the final portfolio to see the differences.


# Gernerating trading signals for both of the strategies
strategy.trade_portfolio(test_data, risk_free_test)
strategy_corr.trade_portfolio(test_data, risk_free_test, long_pct=0.05, short_pct=0.05)


# To check the trading signals for the strategy, we can just use the get_trading_signal method to call the dataframe as below.


# Get trading signal for strategy
strategy.get_trading_signal()


# Now let’s see some examples of equity curves generated by PearsonStrategy. 


def calc_cum_return(strategy):
    """
    Calculates cumulative return of each strategy in testing period.
    
    :param strategy: (PearsonStrategy) A strategy using PearsonStrategy.
    :return: (pd.Series) Series of returns.
    """
    
    # Get trading signals and monthly return on test period
    trading_signal = strategy.get_trading_signal()
    test_monthly_return = strategy.test_monthly_return 

    # Mulitply the both dataframe to get a dataframe of returns with trading signal
    test_traded_return = test_monthly_return*trading_signal

    return_mean_list = [] # Monthly average return list
    
    # Loop through every month to calculate the mean return 
    for month in test_traded_return.index:
        
        month_series = test_traded_return.loc[month]
        # To track the number of stocks traded and the sum of return for each month
        count = 0 # Number of stocks traded
        return_sum = 0 # Sum of the monthly return
        # Loop through every stock in the month
        for stock_return in month_series:

            return_sum += stock_return
            count+=1
        
        # Add mean return for every stock in the month
        return_mean_list.append(return_sum/count)
    
    return_series = pd.Series(return_mean_list, index=test_traded_return.index)
    return_series = return_series.rename('Monthly Return')
    
    return return_series


# For basic strategy, we have a monthly return series as below and the equity curve is given as well. 


calc_cum_return(strategy)


basic_strategy = (calc_cum_return(strategy) + 1).cumprod()
basic_strategy_plot = basic_strategy-1
basic_strategy_plot.plot(title='Pearson Strategy investemnt portfolio equity curve - basic strategy', figsize=(10,5));
print('Investment portfolio value rose to ',basic_strategy.iloc[-1])


# For correlation strategy, we have a monthly return series as below and the equity curve is given as well. 


calc_cum_return(strategy_corr)


corr_strategy = (calc_cum_return(strategy_corr) + 1).cumprod()
corr_strategy_plot = corr_strategy-1
corr_strategy_plot.plot(title='Pearson Strategy investemnt portfolio equity curve - basic strategy', figsize=(10,5));
print('Investment portfolio value rose to ',corr_strategy.iloc[-1])


# ## Conclusion


# This notebook describes the Pearson Strategy class and its functionality. Also, it shows how the stages of the method (pairs portfolio formation and trading signals generation) can be used on real data and that this method can output profitable trading signals.
#
# The algorithms and the descriptions used in this notebook were described the paper by _Chen et al._ __Empirical investigation of an equity pairs trading strategy__  [available here](http://www.pbcsf.tsinghua.edu.cn/research/chenzhuo/paper/Empirical%20Investigation%20of%20an%20Equity%20Pairs%20Trading%20Strategy.pdf). 
#
#
# Key takeaways from the notebook:
#
# - The Pearson distance approach has two work stages - pairs portfolio formation and trading signals generation.
#
# - The Pearson approach works as follows:
#     - First, after data is preprocessed, the method finds pairs for every stock based on the Pearson correlation. 
#     - Then, by using linear regression, setting stock return as independent variable and pairs portfolio return as the dependent variable, the methods set beta as a regression coefficient.
#     - After the pairs portfolio formation period, trading signals can be generated with test data.
#     - The method selects long and short stocks for each month in the testing period by calculating the return divergence for each stock.
#     - Then the trading signals are generated. 
#
# - There can be two different ways of forming pairs portfolios.
#     - By default, the method calculates equally weighted portfolios.
#     - However, it can also calculates the portfolio return weighted by its pairs correlation coefficients.


# ## References ##
# - [Chen, H., Chen, S., Chen, Z. and Li, F., 2019. Empirical investigation of an equity pairs trading strategy. Management Science, 65(1), pp.370-389.](http://www.pbcsf.tsinghua.edu.cn/research/chenzhuo/paper/Empirical%20Investigation%20of%20an%20Equity%20Pairs%20Trading%20Strategy.pdf)
# - [Perlin, M.S., 2009. Evaluation of pairs-trading strategy at the Brazilian financial market. Journal of Derivatives & Hedge Funds, 15(2), pp.122-136.](https://link.springer.com/article/10.1057/jdhf.2009.4)
# - [Krauss, C., 2017. Statistical arbitrage pairs trading strategies: Review and outlook. Journal of Economic Surveys, 31(2), pp.513-545.](https://www.econstor.eu/bitstream/10419/116783/1/833997289.pdf)

