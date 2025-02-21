# Generated from: pca_approach.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# * Reference: __Statistical Arbitrage in the U.S. Equities Market__ _by_ Marco Avellaneda and Jeong-Hyun Lee


# # PCA Approach


# This description of the PCA approach closely follows the work of _Marco Avellaneda_ and _Jeong-Hyun Lee_ __Statistical Arbitrage in the U.S. Equities Market__  [available here](https://math.nyu.edu/faculty/avellane/AvellanedaLeeStatArb20090616.pdf). 


# ## Introduction


# This research notebook shows how the Principal Component Analysis can be used to create mean-reverting portfolios
# and generate trading signals. It's done by considering residuals or idiosyncratic components
# of returns and modeling them as mean-reverting processes.
#
# The original paper presents the following description:
#
# The returns for different stocks are denoted as $\{ R_{i} \}^{N}_{i=1}$. The $F$ represents
# the return of a "market portfolio" over the same period. For each stock in the universe:
#
# $$R_{i} = \beta_{i} F + \tilde{R_{i}}$$
#
# which is a regression, decomposing stock returns into a systematic component $\beta_{i} F$ and
# an (uncorrelated) idiosyncratic component $\tilde{R_{i}}$.
#
# This can also be extended to a multi-factor model with $m$ systematic factors:
#
# $$R_{i} = \sum^{m}_{j=1} \beta_{ij} F_{j} + \tilde{R_{i}}$$
#
# A trading portfolio is a market-neutral one if the amounts $\{ Q_{i} \}^{N}_{i=1}$ invested in
# each of the stocks are such that:
#
# $$\bar{\beta}_{j} = \sum^{N}_{i=1} \beta_{ij} Q_{i} = 0, j = 1, 2,, ..., m.$$
#
# where $\bar{\beta}_{j}$ correspond to the portfolio betas - projections of the
# portfolio returns on different factors.
#
# As derived in the original paper,
#
# $$\sum^{N}_{i=1} Q_{i} R_{i} = \sum^{N}_{i=1} Q_{i} \tilde{R_{i}}$$
#
# So, a market-neutral portfolio is only affected by idiosyncratic returns.


# ## PCA Approach
#
#
# This approach was originally proposed by Jolliffe (2002). It is using a historical share price data
# on a cross-section of $N$ stocks going back $M$ days in history. The stocks return data
# on a date $t_{0}$ going back $M + 1$ days can be represented as a matrix:
#
# $$R_{ik} = \frac{S_{i(t_{0} - (k - 1) \Delta t)} - S_{i(t_{0} - k \Delta t)}}{S_{i(t_{0} - k \Delta t)}}; k = 1, ..., M; i = 1, ..., N.$$
#
# where $S_{it}$ is the price of stock $i$ at time $t$ adjusted for dividends. For
# daily observations $\Delta t = 1 / 252$.
#
# Returns are standardized, as some assets may have greater volatility than others:
#
# $$Y_{ik} = \frac{R_{ik} - \bar{R_{i}}}{\bar{\sigma_{i}}}$$
#
# where
#
# $$\bar{R_{i}} = \frac{1}{M} \sum^{M}_{k=1}R_{ik}$$
#
# and
#
# $$\bar{\sigma_{i}}^{2} = \frac{1}{M-1} \sum^{M}_{k=1} (R_{ik} - \bar{R_{i}})^{2}$$
#
# And the empirical correlation matrix is defined by
#
# $$\rho_{ij} = \frac{1}{M-1} \sum^{M}_{k=1} Y_{ik} Y_{jk}$$
#
# **Note:** It's important to standardize data before inputting it to PCA, as the PCA seeks to maximize the
# variance of each component. Using unstandardized input data will result in worse results.
# The *get_signals()* function in this module automatically standardizes input returns before
# feeding them to PCA.
#
# The original paper mentions that picking long estimation windows for the correlation matrix
# ($M \gg N$, $M$ is the estimation window, $N$ is the number of assets in a portfolio)
# don't make sense because they take into account the distant past which is economically irrelevant.
# The estimation windows used by the authors is fixed at 1 year (252 trading days) prior to the trading date.
#
# The eigenvalues of the correlation matrix are ranked in the decreasing order:
#
# $$N \ge \lambda_{1} \ge \lambda_{2} \ge \lambda_{3} \ge ... \ge \lambda_{N} \ge 0.$$
#
# And the corresponding eigenvectors:
#
# $$v^{(j)} = ( v^{(j)}_{1}, ..., v^{(j)}_{N} ); j = 1, ..., N.$$
#
# Now, for each index $j$ we consider a corresponding "eigenportfolio", in which we
# invest the respective amounts invested in each of the stocks as:
#
# $$Q^{(j)}_{i} = \frac{v^{(j)}_{i}}{\bar{\sigma_{i}}}$$
#
# And the eigenportfolio returns are:
#
# $$F_{jk} = \sum^{N}_{i=1} \frac{v^{(j)}_{i}}{\bar{\sigma_{i}}} R_{ik}; j = 1, 2, ..., m.$$


from IPython.display import Image
Image(filename='PCA/pca_approach_portfolio.png')


# *Performance of a portfolio composed using the PCA approach in comparison to the market cap portfolio.
# An example from ["Statistical Arbitrage in the U.S. Equities Market"](https://math.nyu.edu/faculty/avellane/AvellanedaLeeStatArb20090616.pdf)
# by Marco Avellaneda and Jeong-Hyun Lee.*


# In a multi-factor model we assume that stock returns satisfy the system of stochastic
# differential equations:
#
# $$\frac{dS_{i}(t)}{S_{i}(t)} = \alpha_{i} dt + \sum^{N}_{j=1} \beta_{ij} \frac{dI_{j}(t)}{I_{j}(t)} + dX_{i}(t),$$
#
# where $\beta_{ij}$ are the factor loadings.
#
# The idiosyncratic component of the return with drift $\alpha_{i}$ is:
#
# $$d \widetilde{X_{i}}(t) = \alpha_{i} dt + d X_{i} (t).$$
#
# Based on the previous descriptions, a model for $X_{i}(t)$ is estimated as the Ornstein-Uhlenbeck
# process:
#
# $$dX_{i}(t) = \kappa_{i} (m_{i} - X_{i}(t))dt + \sigma_{i} dW_{i}(t), \kappa_{i} > 0.$$
#
# which is stationary and auto-regressive with lag 1.
#
# The parameters $\alpha_{i}, \kappa_{i}, m_{i}, \sigma_{i}$ are specific for each stock.
# They are assumed to *de facto* vary slowly in relation to Brownian motion increments $dW_{i}(t)$,
# in the chosen time-window. The authors of the paper were using a 60-day window to estimate the residual
# processes for each stock and assumed that these parameters were constant over the window.
#
# However, the hypothesis of parameters being constant over the time-window is being accepted
# for stocks which mean reversion (the estimate of $\kappa$) is sufficiently high and is
# rejected for stocks with a slow speed of mean-reversion.
#
# An investment in a market long-short portfolio is being constructed by going long 1 dollar on the stock and
# short $\beta_{ij}$ dollars on the $j$ -th factor. Expected 1-day return of such portfolio
# is:
#
# $$\alpha_{i} dt + \kappa_{i} (m_{i} - X_{i}(t))dt$$
#
# The parameter $\kappa_{i}$ is called the speed of mean-reversion. If $\kappa \gg 1$ the
# stock reverts quickly to its means and the effect of drift is negligible. As we are assuming that
# the parameters of our model are constant, we are interested in stocks with fast mean-reversion,
# such that:
#
# $$\frac{1}{\kappa_{i}} \ll T_{1}$$
#
# where $T_{1}$ is the estimation window to estimate residuals in years.


# ## PCA Trading Strategy
#
# The strategy implemented in the ArbitrageLab module sets a default estimation window for the correlation
# matrix as 252 days, a window for residuals estimation of 60 days ($T_{1} = 60/252$) and the
# threshold for the mean reversion speed of an eigenportfolio for it to be traded so that the reversion time
# is less than $1/2$ period ($\kappa > 252/30 = 8.4$).
#
# For the process $X_{i}(t)$ the equilibrium variance is defined as:
#
# $$\sigma_{eq,i} = \frac{\sigma_{i}}{\sqrt{2 \kappa_{i}}}$$
#
# And the following variable is defined:
#
# $$s_{i} = \frac{X_{i}(t)-m_{i}}{\sigma_{eq,i}}$$
#
# This variable is called the S-score. The S-score measures the distance to the equilibrium of the cointegrated
# residual in units standard deviations, i.e. how far away a given asset eigenportfolio is from the theoretical
# equilibrium value associated with the model.


Image(filename='PCA/pca_approach_s_score.png')


# *Evolution of the S-score of JPM ( vs. XLF ) from January 2006 to December 2007.
# An example from  ["Statistical Arbitrage in the U.S. Equities Market"](https://math.nyu.edu/faculty/avellane/AvellanedaLeeStatArb20090616.pdf)
# by Marco Avellaneda and Jeong-Hyun Lee.*


# If the eigenportfolio shows a mean reversion speed above the set threshold ($\kappa$), the
# S-score based on the values from the residual estimation window is being calculated.
#
# The trading signals are generated from the S-scores using the following rules:
#
# - Open a long position if $s_{i} < - \bar{s_{bo}}$
#
# - Close a long position if $s_{i} < + \bar{s_{bc}}$
#
# - Open a short position if $s_{i} > + \bar{s_{so}}$
#
# - Close a short position if $s_{i} > - \bar{s_{sc}}$
#
# Opening a long position means buying 1 dollar of the corresponding stock (of the asset eigenportfolio)
# and selling $\beta_{i1}$ dollars of assets from the first scaled eigenvector ($Q^{(1)}_{i}$),
# $\beta_{i2}$ from the second scaled eigenvector ($Q^{(2)}_{i}$) and so on.
#
# Opening a short position, on the other hand, means selling 1 dollar of the corresponding stock and buying
# respective beta values of stocks from scaled eigenvectors.
#
# Authors of the paper, based on empirical analysis chose the following cutoffs. They were selected
# based on simulating strategies from 2000 to 2004 in the case of ETF factors:
#
# - $\bar{s_{bo}} = \bar{s_{so}} = 1.25$
#
# - $\bar{s_{bc}} = 0.75$, $\bar{s_{sc}} = 0.50$
#
# The rationale behind this strategy is that we open trades when the eigenportfolio shows good mean
# reversion speed and its S-score is far from the equilibrium, as we think that we detected an anomalous
# excursion of the co-integration residual. We expect most of the assets in our portfolio to be near
# equilibrium most of the time, so we are closing trades at values close to zero.
#
# The signal generating function implemented in the ArbitrageLab package outputs target weights for each
# asset in our portfolio for each observation time - target weights here are the sum of weights of all
# eigenportfolios that show high mean reversion speed and have needed S-score value at a given time.


# ## Usage of the Algorithms


# Let's use the above tools on real data. 
#
# First, we will choose a set of stocks to apply the PCA approach to. Then we will go through the steps of the PCA approach and we'll generate trading signals using the PCA Strategy. Finally, we will analyze the obtained results. 


import arbitragelab as al
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# ### Loading data


# We picked a set containing 176 stocks to apply the PCA Approach to. We'll be looking at a period of years 2018-2019. We'll eventually get trading signals for the year 2019, as the observations from the year 2018 will be needed to estimate the correlation matrix to get the PCA components.  


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
data =  yf.download(tickers, start="2018-01-03", end="2019-12-31")

# Taking close prices for chosen instruments
data = data["Adj Close"]

# Looking at the downloaded data
data.head()


# As our method takes in returns, we'll calculate them from our dataframe of prices
returns = data.pct_change()[1:]

# Looking at the obtrined returns series
returns.head()


# We will go now through the steps of calculating S-scores for a window of observations to explain how the PCA approach works and will then generate treading signals.


# Starting with setting a PCAStrategy class with 15 principal components
pca_strategy = al.other_approaches.PCAStrategy(n_components=15)


# To get the factor weights from PCA we'll be using a window with 252 observations as in the original paper
data_252days = returns[:252]

# We can standardize our data
standardized_252days = pca_strategy.standardize_data(data_252days)

# But the function for calculation of the factor weights using PCA will do it by itself
factorweights = pca_strategy.get_factorweights(data_252days)

# Looking at the factor weights
factorweights


# Our factor weights are 15 first components from the PCA divided by the standard deviations of returns of our assets.
#
# Now we can get a 60-day window of observations to calculate residuals and coefficients. The calculation is done by fitting a linear regression on the returns from this window and factor returns from this window.


# Getting a 60-day window of observations to calculate factor returns
data_60days = returns[(252-60):252]

# Last day in our window
data_60days.index[-1]


# Calculating factor returns from our returns - multiplying them by factor weights
factorret = pd.DataFrame(np.dot(data_60days, factorweights.transpose()), index=data_60days.index)

# Looking at the obtained factor returns
factorret.head()


# So for each component from PCA and for each observation we get a return value. 


# Now fitting the linear regression to get residuals and coefficients of the regression
residual, coefficient = pca_strategy.get_residuals(data_60days, factorret)

# Residuals dataframe
residual.head()


# Coefficients dataframe
coefficient


# Using each column in the residuals dataframe we'll decide whether to trade an eigenportfolio related to that asset.
# The eigenportfolio will be used if:
#
#     a) the mean reversion speed of the OU process composed from the residuals is high enough,
#
#     b) the OU process deviates enough from its mean value.
#
# So, in our example, we can have up to 176 eigenportfolios. After the checks for the mean reversion speed and the S-scores are
# made we might end up with about 10 eigenportfolios that are suitable to be traded. 
#
# Using the betas - values from the coefficients dataframe the eigenportfolio will be constructed. 
#
# For example, if we have a signal to go long on the **AA** asset eigenportfolio and we use a scaling parameter equal to one, we
# will:
# - go long one dollar of the **AA** asset;
# - go short the **A** stock with the sum of betas from the **A** column (*coefficient* dataframe);
# - go short the **AA** stock with the sum of betas from the **AA** column (*coefficient* dataframe);
# - go short the **AAPL** stock with the sum of betas from the **AAPL** column (*coefficient* dataframe);
# - and so on..
#
# for each stock in a portfolio.


# Now, calculating the S-scores
s_scores = pca_strategy.get_sscores(residual, k=8.4)

# Picking parameters to trade based on the S-score
sbo = 1.25
sso = 1.25
ssc = 0.5
sbc = 0.75

# Stock eigenportfolios that we should long
s_scores[s_scores < -sbo]


# Stock eigenportfolios that we should short
s_scores[s_scores > sso]


# So these are the S-scores for each eigenportfolio. We've printed those of them that are either above or below critical values
# to enter a trade.
#
# We should go long on 19 eigneportfolios and short on 15 eigenportfolios for this observation.
#
# To calculate these S-scores we estimated the PCA components on the 252 trading days of the year 2018 and
# calculated the residuals on the last 60 days of the year 2018. The last observation used for the estimation was
# 2019.01.02. So these trading signals can be used on 2019.01.03.
#
# By moving the 60-day window one observation ahead and recalculating the residuals and the regression coefficients
# we would get new S-scores and based on them we would have a trading signal for 2019.01.04.
#
# As the estimated correlation matrix used to get the PCA factors doesn't change much, it's calculated again only once
# we generated the whole residual window of signals. So in our example, it would be recalculated every 60 days using the
# last 252 observations.


# Now we can simply use the PCA Strategy with a single function and given input parameters to generate trading signals
#
# **Note:** This function can be used on the raw returns dataframe. The previous steps are presented in the notebook
# to explain the idea behind the PCA Strategy.
#
# This function might take a long time to generate output, especially if given a dataframe with a big number of observations, as
# to generate trading signals for a single day we have to go through the all steps mentioned above.


# Simply applying the PCAStrategy with standard parameters
target_weights = pca_strategy.get_signals(returns, k=8.4, corr_window=252,
                                          residual_window=60, sbo=1.25,
                                          sso=1.25, ssc=0.5, sbc=0.75,
                                          size=1)



# Looking at generated trading signals
target_weights.head()


# Now, let's normalize these weights - so that on each day we'd be long or short a sum of 1 asset units. 


# Normalizing weights
norm_weights = target_weights.divide(abs(target_weights).sum(axis=1), axis=0)

# Checking if the sum of absolute weights for each date is 1
abs(norm_weights).head().sum(axis=1)


# Returns dataframe
returns_test = returns[(252 - 1):-1]

# Checking that our returns dataframe have the same index as the trading signals dataframe
returns_test.head()


# Shifting the trading signal dataframe one observation further,
# as we would be able to use those signals on the following day
investment_portfolio_returns = (returns_test * norm_weights.shift(1)).sum(axis=1)

# Calculating the portfolio price of our investment portfolio
investment_portfolio_price = (investment_portfolio_returns + 1).cumprod()

# And calculating the equity curve of our investment portfolio
equity_curve = investment_portfolio_price  - 1


# Plotting the equity curve
equity_curve.plot(figsize = (20,7),
                  title='PCA Strategy investment portfolio equity curve');


# These results look good, over the year 2019 equity curve shows an increase in the investment portfolio value from 1 to around 1,1. 
#
# We can further test this strategy by choosing different critical values for the S-score, increasing the mean reversion speed threshold, or adding transaction costs to see if the strategy is robust.


# ## Conclusion


# This notebook describes the PCA Strategy class and its functionality. Also, it shows how the tools can be used on real data.
#
# The algorithms used in this notebook were described by _Marco Avellaneda_ and _Jeong-Hyun Lee_ in the paper __Statistical Arbitrage in the U.S. Equities Market__  [available here](https://math.nyu.edu/faculty/avellane/AvellanedaLeeStatArb20090616.pdf).
#
# Key takeaways from the notebook:
# - Principal Component Analysis can be used to create mean-reverting portfolios and generate trading signals.
# - First, a window of 252 observations is used to get an empirical correlation matrix and use the PCA to get N top components.
# - It’s important to standardize data before inputting it to PCA, as the PCA seeks to maximize the variance of each component.
# - A separate market-neutral eigenportfolio can be calculated for each stock in our portfolio.
# - Next, we pick a window to calculate residuals (60 days in the example).
# - By using linear regression on the second window (60-days) and factor returns for this window we get residuals and the coefficients of regression.
# - These residuals are used to construct an OU process for each eigenportfolio.
# - If the OU process shows a high (above the $\kappa$ threshold) speed of mean reversion, we calculate the s-score for it.
# - S-score is measuring how far away a given asset eigenportfolio is from the theoretical equilibrium value associated with the model.
# - If the S-score is too high or too low we generate a signal to sell or buy this eigenportfolio.
# - Resulting trading signal is the sum of all eigenportfolio weights that satisfy the requirements to be traded.
# - Parameters to optimize in this strategy are the mean reversion speed threshold, the windows for PCA and residual calculation, and the S-score thresholds to enter or exit positions. 

