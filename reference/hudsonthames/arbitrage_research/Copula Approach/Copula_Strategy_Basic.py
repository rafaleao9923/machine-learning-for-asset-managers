# Generated from: Copula_Strategy_Basic.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Copula Pair's Trading Basic Strategy
#
# This notebook demonstrates the usage of the `BasicCopulaTradingRule` from the Trading Strategies module.
# The framework is originally proposed in 
# - Liew, Rong Qi, and Yuan Wu. "Pairs trading: A copula approach."
# - Stander, Yolanda, Daniël Marais, and Ilse Botha. "Trading strategies with copulas."
#
# ## A Bare Minimum Intro to Copula
#
# ### What Merit Does It Have
# Consider having a pair of cointegrated stocks. 
# By analyzing their time series, one can calculate their standardized price gap as part of a distance approach, or project their long-run mean as in a cointegrated system as part of a cointegration approach. 
# However, none of the two methods are built with the assumptions on distributions from the stocks' time series, which may lead to unused information.
# Further, just using a single parameter (i.e., Euclidean distance) to quantify two coupled time series might have fundamentally simplified the problem too much.
# The copula model naturally incorporates their marginal distributions, together with other interesting properties from each copula inherited from their own structures, e.g., tail dependency for capturing rare and/or extreme moments like large, cointegrated swings in the market.
#
# Briefly speaking, a copula is a tool to capture details of how two random variables are “correlated”.
# By having a more detailed modeling framework, we expect the pairs trading strategy followed to be more realistic and robust, and possibly to bring more trading opportunities.


# ### Definitions for Bivariate Copula
# (**Definition using Sklar's Theorem**) For two random variables $S_1$, $S_2 \in [-\infty, \infty]$.
# $S_1$ and $S_2$ have their own fixed, continuous CDFs $F_1, F_2$.
# Consider their (cumulative) joint distribution $H(s_1, s_2) := P(S_1 \le s_1, S_2 \le s_2)$.
# Now take the uniformly distributed quantile random variable $U_1(S_1)$, $U_2(S_2)$, for every pair
# $(u_1, u_2)$ drawn from the pair's quantile we define the **bivariate copula**
# $C: [0, 1] \times [0, 1] \rightarrow [0, 1]$ as:
#
# $$
#     \begin{align}
#     C(u_1, u_2) &= P(U_1 \le u_1, U_2 \le u_2) \\
#     &= P(S_1 \le F_1^{-1}(u_1), S_2 \le F_2^{-1}(u_2)) \\
#     &= H(F_1^{-1}(u_1), F_2^{-1}(u_2))
#     \end{align}
# $$
# where $F_1^{-1}$ and $F_2^{-1}$ are quasi-inverse of the marginal CDFs $F_1$ and $F_2$.
# The definition, although mathematically more fundamental, is not used as much in trading.
# Instead, cumulative conditional probabilities and copula density are used more often, which we will define as below:
#
# ### Conditional Probabilities
# $$
#     \begin{align}
#     P(U_1\le u_1 | U_2 = u_2) &:= \frac{\partial C(u_1, u_2)}{\partial u_2}, \\
#     P(U_2\le u_2 | U_1 = u_1) &:= \frac{\partial C(u_1, u_2)}{\partial u_1}.
#     \end{align}
# $$
# ### Copula Density
#
# $$
#     c(u_1 , u_2) := \frac{\partial^2 C(u_1, u_2)}{\partial u_1 \partial u_2},
# $$
# which by definition is the probability density.
#
# For interested readers, Nelsen's book [An Introduction to Copulas](https://www.springer.com/gp/book/9780387286594) and note [Properties and applications of copulas: A brief survey](http://w4.stern.nyu.edu/ioms/docs/sg/seminars/nelsen.pdf) presents more rigorously and thoroughly on the subject.


# ## Basic Strategy (Conditional Probabilities Threshold)
#
# ### Logic
# This was originally proposed in [Liew et al., 2013] and [Stander et al., 2013].
# We start with a pair of stocks of interest $S_1$ and $S_2$, which can be selected by various methods.
# For example, using the Engle-Granger test for cointegration.
# By consensus, we define the spread as $S_1$ in relation to $S_2$.
# e.g. Short the spread means buying $S_1$ and/or selling $S_2$.
#
# Use **cumulative log return** data of the stocks during the training/formation period, we proceed with a **pseudo-MLE** fit to establish a copula that reflects the relation of the two stocks during the training/formation period.
#
# **Note**: <br>
# the type of processed data fed in need to be **approximately stationary**.
# i.e., $\mathbb{E}[X(t_1)] \approx \mathbb{E}[X(t_2)]$ for time series $X$, for all $t_1, t_2$ in
# the scope of interest.
# For example, if we model each stock's price to have a log-Normal distribution, then the price itself cannot be stationary after some time.
# Using cumulative log return has the same issue if the time span is sufficiently long.
# One can consider just using the daily return or its logarithm instead, given that the stock's price has a log-Normal distribution. i.e., $\frac{X(t+1)}{X(t)}$ or $\ln \left( \frac{X(t+1)}{X(t)} \right)$.
#
# - $u_i \in [0, 1]$ is the quantile of trading period data mapped by a CDF formed in the training period.
# - When $P(U_1\le u_1 | U_2 = u_2) < 0.5$, then stock 1 is considered under-valued.
# - When $P(U_1\le u_1 | U_2 = u_2) > 0.5$, then stock 1 is considered over-valued.
#
# Now we define an upper threshold $b_{up}$ (e.g. $0.95$) and a lower threshold $b_{lo}$ (e.g. $0.05$),
# then the logic goes as follows:
#
# - If $P(U_1\le u_1 | U_2 = u_2) \le b_{lo}$ and $P(U_2\le u_2 | U_1 = u_1) \ge b_{up}$, then stock 1 is
#   undervalued, and stock 2 is overvalued. Hence we long the spread.
# - If $P(U_2\le u_2 | U_1 = u_1) \le b_{lo}$ and $P(U_1\le u_1 | U_2 = u_2) \ge b_{up}$, then stock 2 is
#   undervalued, and stock 1 is overvalued. Hence we short the spread.
# - If **both/either** conditional probabilities cross the boundary of $0.5$, then we exit the position, as we consider the position no longer valid.


# ### Ambiguities and Comments
# The authors did not specify what will happen if the followings occur:
#
# 1. When there is an open signal and an exit signal.
# 2. When there is an open signal and currently there is a position.
# 3. When there is a long and short signal together.
#
# Here is our take:
#
# 1. Exit signal overrides open signal.
# 2. Flip the position to the signal's suggestion. For example, originally have a short position, and receives
#    a long signal, then the position becomes long.
# 3. Technically this should never happen with the default trading logic. However, if it did happen for whatever 
#    reason, long + short signal will lead to no opening signal and the positions will not change, unless there
#    is an exit signal and that resets the position to 0.
#
# For exiting a position, the authors proposed using **'and'** logic: Both conditional probabilities need to cross $0.5$.
# However, we found this too strict and sometimes fails to exit a position when it should.
# Therefore we also provide the **'or'** logic: At least one of the conditional probabilities cross $0.5$.


# ### `BasicCopulaTradingRule` Class Functionalities
#
# Tools presented in this module enable the user to:
#
#   - Fit a selected copula to a training dataset (i.e., data from 2016-2019) and generate emirical CDFs.
#   - Feed in single observations one-by-one (i.e., EOD data from just today) and check if the strategy generates a signal.
#   - If a signal is generated, the position can be opened and added to an internal dictionary of the class that tracks positions.
#   - At any time it's possible to check if the trategy generates a signal to close any of the opened positions. If so, ID's of these positions will be returned and the internal dictionary of the class withh be updated.
#
# There are 8 commonly used pure copulas that are now available: `Gumbel`, `Frank`, `Clayton`, `Joe`, `N13`, 
# `N14`, `GaussianCopula`, and `StudentCopula` (Student-t), and 2 mixed copulas `CFGMixCop` (Clayton-Frank-Gumbel) and 
# `CTGMixCop` (Clayton-Student-Gumbel).
# They are all subclasses of the class `Copula` and `MixedCopula`, and they share some common repertoire of methods and attributes.
#
# The user can chose the appropriate copula, fit data to it and then use it in the trading strategy. This modular approach makes it easier to construct multiple strategies and test hypothesis easier.
#
# The user may choose to fit the pair's data to all provided copulas, then compare the information criterion scores (AIC,
# SIC, HQIC, Log-likelihood) to decide the best copula. One can further use the fitted copula to generate trading positions by giving thresholds from data.
#
# **Very Important Note**:<br>
# For `StudentCopula`, the user can choose to provide the degrees of freedom parameter $\nu$, as an extra input argument `nu`.
# Use $\nu = \text{sample size} - 1$ is strongly discouraged, as data from time series are clearly not mutually independent instances. For $\nu > 12$, consider using the `GaussianCopula` instead.
#
# Mixed copulas especially `CTGMixCop` is relatively slow to fit. However, it generally provides the best log-likelihood score.


# ### `copula_calculation` Module
# To be able to calculate marginal CDFs (quantile function) for plotting purposes or processing other data to be able to feed to some copula, one may use its `construct_ecdf_lin` function.
# It is a wrapper around `ECDF` function from `statsmodels`, and allows linear interpolation between points instead of using a step function as `ECDF`.
#
# This function finds an empirical CDF based on given training data, and does not generate $0$ or $1$, instead gives numbers sufficiently close to $0$ and $1$.
# This is done because when some copulas take values in $0$ or $1$, the calculation of density and/or marginal conditional probability may suffer numerical issues.
#
# ## Usage
# The demonstration part has the following sections using real-world data:
# 1. Importing and Data Pre-processing.
# 2. Fitting Data to Different Copulas with Training Data.
# 3. Generating Trading Positions using Testing Data.
# 4. Possible Issues Discussion.


# ### 1. Importing and Data Pre-processing


# Importing libraries and modules
import pandas as pd
import numpy as np
import datetime as dt  # For plotting x-axis as dates
import matplotlib.pyplot as plt
import statsmodels.api as sm

from arbitragelab.trading import BasicCopulaTradingRule
import arbitragelab.copula_approach.copula_calculation as ccalc
from arbitragelab.copula_approach.archimedean import (Gumbel, Clayton, Frank, Joe, N13, N14)
from arbitragelab.copula_approach.elliptical import (StudentCopula, GaussianCopula)


# For the copula approach to work, the stocks pair need to be cointegrated to begin with.
# Here we choose BKD and ESC, the same as the author, and use their daily closing price from the start of 2009 to the end of 2012.
# Note that the original price series is not what the copula will use. Instead, we use cumulative return data implied from the price series.


# Importing data
pair_prices = pd.read_csv(r'BKD_ESC_2009_2011.csv', index_col=0, parse_dates=True)


# Now we take a look at the price series for the whole period.
# They indeed have cointegrated behavior at first glance.
# We then do a training and testing split to fit and simulate trading.


# Plotting data
plt.figure(dpi=120)
plt.plot(pair_prices['BKD'], label='BKD')
plt.plot(pair_prices['ESC'], label='ESC')
plt.axvline(dt.date(2012, 1, 3), color='red')  # Training testing split date
plt.legend()
plt.grid()
plt.gcf().autofmt_xdate()
plt.title(r'Original Price Series of BKD and ESC')
plt.show()


# Initiate the analysis module
BCS = BasicCopulaTradingRule()

# Training and testing split
training_length = 756 # From 01/02/2009 to 12/30/2011 (m/d/y)

prices_train = pair_prices.iloc[: training_length]
prices_test = pair_prices.iloc[training_length :]

# Empirical CDF for the training set.
# This step is only necessary for plotting.
cdf1 = ccalc.construct_ecdf_lin(prices_train['BKD'])
cdf2 = ccalc.construct_ecdf_lin(prices_train['ESC'])


# ### 2. Fitting Data to Different Copulas with Training Data.
# Here we fit to every copula type available in the module, and print out the scores in terms of SIC, AIC, and HQIC. The lower the score (Note they are all negative), the better the fit.
#
# **Note**:<br>
# 1. `fit_copula_to_empirical_data` returns the fit result, the fitted copula, and marginal CDFs for the two input lists. Here the `cdf1`, `cdf2` is exactly the same as directly using `construct_ecdf_lin` function in `copula_calculation` module.
# 2. For `Student` copula, the MLE of $\nu$ is slow.
# 3. For mixed copulas, the fit is slow however they generally gives the best score.
# 4. You may need to tune the fitting parameters for mixed copulas: gamma_scad, a_scad to avoid warnings outputs.


# Fit different copulas, store the results in dictionaries
fit_result_gumbel, copula_gumbel, cdf_x_gumbel, cdf_y_gumbel =\
    ccalc.fit_copula_to_empirical_data(x=prices_train['BKD'], y=prices_train['ESC'], copula=Gumbel)

fit_result_frank, copula_frank, cdf_x_frank, cdf_y_frank =\
    ccalc.fit_copula_to_empirical_data(x=prices_train['BKD'], y=prices_train['ESC'], copula=Frank)

fit_result_clayton, copula_clayton, cdf_x_clayton, cdf_y_clayton =\
    ccalc.fit_copula_to_empirical_data(x=prices_train['BKD'], y=prices_train['ESC'], copula=Clayton)

fit_result_joe, copula_joe, cdf_x_joe, cdf_x_joe=\
    ccalc.fit_copula_to_empirical_data(x=prices_train['BKD'], y=prices_train['ESC'], copula=Joe)

fit_result_n14, copula_n14, cdf_x_n14, cdf_y_n14=\
    ccalc.fit_copula_to_empirical_data(x=prices_train['BKD'], y=prices_train['ESC'], copula=N14)

fit_result_gauss, copula_gauss, cdf_x_gauss, cdf_y_gauss =\
    ccalc.fit_copula_to_empirical_data(x=prices_train['BKD'], y=prices_train['ESC'], copula=GaussianCopula)

fit_result_t, copula_t, cdf_x_t, cdf_y_t=\
    ccalc.fit_copula_to_empirical_data(x=prices_train['BKD'], y=prices_train['ESC'], copula=StudentCopula)


# **Note**: The warnings generated above is due to the optimization package by scipy not strictly following the prescribed bounds in the mixed copula fitting algo. And based on our experiments it does not influence the fit result with statistical significance. To completely get rid of the warnings, you will need to choose specific values `gamma_scad` and `a_scad` of the fitting parameter, and this heavily depends on the data."


# Print all the fit scores
print(fit_result_gumbel)
print(fit_result_frank)
print(fit_result_clayton)
print(fit_result_joe)
print(fit_result_n14)
print(fit_result_gauss)
print(fit_result_t)


# It seems by the score, Student-t and Gaussian are reasonable choices of copula that fit our training data the best.
# Clayton also looks somewhat reasonable, although the tail dependency on the upper right corner is not taken into account.
# So at first, we take a look at their information.


# Print copula descriptions
print(copula_t.describe(), '\n')
print(copula_gauss.describe(), '\n')
print(copula_clayton.describe(), '\n')


# Now we plot the training data (as an empirical copula), together with $5$ other copulas fitted.


# Plotting copulas
fig, ax = plt.subplots(figsize=(5,7), dpi=100)

ax.scatter(prices_train['BKD'].apply(cdf1), prices_train['ESC'].apply(cdf2), s=1)
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'Empirical from BKD and ESC, Training Data')
ax.set_xlim([-0.02, 1.02])
ax.set_ylim([-0.02, 1.02])
plt.tight_layout()


# N14
copula_n14.plot_scatter(num_points=training_length);


# Student-t
copula_t.plot_scatter(num_points=training_length);


# Joe
copula_joe.plot_scatter(num_points=training_length);


# Frank
copula_frank.plot_scatter(num_points=training_length);


# Gumbel
copula_gumbel.plot_scatter(num_points=training_length);


# Clayton
copula_clayton.plot_scatter(num_points=training_length);


# Gaussian
copula_gauss.plot_scatter(num_points=training_length);


# ### 3. Generate Trading Positions Using Test Data
# At first, we plot the testing data (as an empirical copula) and the two chosen copulas.


# Plotting copulas
fig, ax = plt.subplots(figsize=(5,7), dpi=100)

ax.scatter(prices_test['BKD'].map(cdf1), prices_test['ESC'].map(cdf2), s=1)
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'Empirical from BKD and ESC, Test Data')
ax.set_xlim([-0.02, 1.02])
ax.set_ylim([-0.02, 1.02])
plt.tight_layout()

test_length = len(prices_test)


# Student-t
copula_t.plot_scatter(num_points=test_length);


# Gaussian
copula_gauss.plot_scatter(num_points=test_length);


# Clayton
copula_clayton.plot_scatter(num_points=test_length);


# Then we get trading positions from the two chosen copulas.
#
# **Note**:<br>
# Although theoretically, one can change the threshold to potentially bring more trading opportunities, it needs to proceed with caution, as the recommended positions are very sensitive to the choice of copula and training data if the thresholds are not as strict.


# #### Trading Simulation
#
# As the trading strategy takes new observations one by one, we'll simulate such process.
#
# So first we use the fitted copulas and CDFs to initialize trading strategies. Then we feed observations one by one, checking if the logic to open a long/short trade is triggered. If so, we take the trade and update the internal dictionary of the trading strategy class.
#
# We also check if any of the currently open positions should be closed, and if so, we again update the internal dictionary.
#
# In the end of the simulation we analyze the opened and closed positions during the period.


# Generate Trading Positions
# Using 'and' logic by default.

# ========== Use Student-t Copula ==========
# Instantiate the strategy
BCTR_t = BasicCopulaTradingRule(exit_rule='and', open_probabilities=(0.5, 0.95),
                                exit_probabilities=(0.9, 0.5))
# Adding copula, cdf for X and Y to strategy
BCTR_t.set_copula(copula_t)
BCTR_t.set_cdf(cdf_x_t, cdf_y_t)
# Setting initial probabilities
BCTR_t.current_probabilities = (0.5, 0.5)

# ========== Use Gaussian Copula ==========
# Instantiate the strategy
BCTR_gauss = BasicCopulaTradingRule(exit_rule='and', open_probabilities=(0.5, 0.95),
                                    exit_probabilities=(0.9, 0.5))
# Adding copula, cdf for X and Y to strategy
BCTR_gauss.set_copula(copula_gauss)
BCTR_gauss.set_cdf(cdf_x_gauss, cdf_y_gauss)
# Setting initial probabilities
BCTR_gauss.current_probabilities = (0.5, 0.5)

# ========== Use Clayton Copula ==========
# Instantiate the strategy
BCTR_clayton = BasicCopulaTradingRule(exit_rule='and', open_probabilities=(0.5, 0.95),
                                      exit_probabilities=(0.9, 0.5))
# Adding copula, cdf for X and Y to strategy
BCTR_clayton.set_copula(copula_clayton)
BCTR_clayton.set_cdf(cdf_x_clayton, cdf_y_clayton)
# Setting initial probabilities
BCTR_clayton.current_probabilities = (0.5, 0.5)

# ========== Use Student-t Copula with 'or' logic ==========
# Instantiate the strategy
BCTR_t_or = BasicCopulaTradingRule(exit_rule='or', open_probabilities=(0.5, 0.95),
                                   exit_probabilities=(0.9, 0.5))
# Adding copula, cdf for X and Y to strategy
BCTR_t_or.set_copula(copula_t)
BCTR_t_or.set_cdf(cdf_x_t, cdf_y_t)
# Setting initial probabilities
BCTR_t_or.current_probabilities = (0.5, 0.5)


# Now we can simulate a trading process, feeding observations one by one to the strategy and checking the outputs.


# Simulate trading process on test data for StudentCopula
for time, values in prices_test.iterrows():
    x_price = values['BKD']
    y_price = values['ESC']

    # Adding price values
    BCTR_t.update_probabilities(x_price, y_price)
    
    # Check if it's time to enter a trade
    trade, side = BCTR_t.check_entry_signal()

    # Close previous trades if needed
    BCTR_t.update_trades(update_timestamp=time)

    if trade:  # Open a new trade if needed
        BCTR_t.add_trade(start_timestamp=time, side_prediction=side)

# Finally, check open trades at the end of the simulation
open_trades_t = BCTR_t.open_trades

# And all trades that were opened and closed
closed_trades_t = BCTR_t.closed_trades


# No currently open trades
len(open_trades_t)


# And 22 trades were opened and closed during the testing period
len(closed_trades_t)


# Getting trades for other strategies.


# Simulate trading process on test data for StudentCopula
for time, values in prices_test.iterrows():
    x_price = values['BKD']
    y_price = values['ESC']

    # Adding price values
    BCTR_gauss.update_probabilities(x_price, y_price)
    BCTR_clayton.update_probabilities(x_price, y_price)
    BCTR_t_or.update_probabilities(x_price, y_price)
    
    # Check if it's time to enter a trade
    trade_gauss, side_gauss = BCTR_gauss.check_entry_signal()
    trade_clayton, side_clayton = BCTR_clayton.check_entry_signal()
    trade_t_or, side_t_or = BCTR_t_or.check_entry_signal()

    # Close previous trades if needed
    BCTR_gauss.update_trades(update_timestamp=time)
    BCTR_clayton.update_trades(update_timestamp=time)
    BCTR_t_or.update_trades(update_timestamp=time)

    if trade_gauss:  # Open a new trade if needed
        BCTR_gauss.add_trade(start_timestamp=time, side_prediction=side_gauss)
    if trade_clayton:  # Open a new trade if needed
        BCTR_clayton.add_trade(start_timestamp=time, side_prediction=side_clayton)
    if trade_t_or:  # Open a new trade if needed
        BCTR_t_or.add_trade(start_timestamp=time, side_prediction=side_t_or)
        
# Finally, check open trades at the end of the simulation
open_trades_gauss = BCTR_gauss.open_trades
open_trades_clayton = BCTR_clayton.open_trades
open_trades_t_or = BCTR_t_or.open_trades

# And all trades that were opened and closed
closed_trades_gauss = BCTR_gauss.closed_trades
closed_trades_clayton = BCTR_clayton.closed_trades
closed_trades_t_or = BCTR_t_or.closed_trades


# Let's look at one of the `closed_trades` logs


closed_trades_gauss


# ## Strategy outputs
#
# We can see the following data:
#
# * Dictionary key:
#   * Timestamp at which the trade was opened
# * Dctionary value:
#   * t1: Timestamp at which the trade was closed
#   * exit_proba: Conditional probabilities of X and Y at which the trade was closed
#   * uuid: Trade ID that can be provided for each trade
#   * side: Side of the trade '-1' for short and '1' for long
#   * initial_proba: Conditional probabilities of X and Y at which the trade was opened
#
# We can see that trades were opened starting from late April 2012 and were all closed at the end of July 2012. They can be treated as multiple trades, or we can follow a logic of only one open trade at a time.
#
# This strategy can be adjusted by choosing different open and close probabilities.


# Following a logic of one open trade at a time - using the first trade
open_time = list(closed_trades_gauss.keys())[0]
close_time = list(closed_trades_gauss.values())[0]['t1']
position = list(closed_trades_gauss.values())[0]['side']

# Creating dataframe for viaualization
positions_gauss = pd.DataFrame(0, index=prices_test.index, columns=['Gauss Positions'])
positions_gauss[(open_time < positions_gauss.index) & (positions_gauss.index< close_time)] = position


# Plotting generated positions
fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 0.7]}, figsize=(10,6), dpi=150)
fig.suptitle('Copula Trading Strategy Results')

# Plotting repositioned log prices
axs[0].plot((prices_test['BKD'] / prices_test['BKD'][0]).map(np.log), label='BKD', color='cornflowerblue')
axs[0].plot((prices_test['ESC'] / prices_test['ESC'][0]).map(np.log), label='ESC', color='seagreen')
axs[0].title.set_text('Repositioned Log Prices')
axs[0].legend()
axs[0].grid()

# Plotting position from Gaussian copula strategy
axs[1].plot(positions_gauss , label='Positions', color='darkorange')
axs[1].title.set_text('Positions from Gaussian Copula, AND logic')
axs[1].set_yticks([-1,0,1])

fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Avoid title overlap
plt.show()


# #### Equity Curve for the Portfolio
# 1. Defining weights (hedging ratio)
# 2. Calculating returns
# 3. Portfolio prices
# 4. Equity curve for copula strategy
#
# There are multiple methods to define weights.
# For example, using OLS or Johansen test on training data.
# Here we define weights as below to reflect the (repositioned) series mentioned above:
# At first, we define the unnormalized weight $w_{1}^* = w_{BKD}$ and $w_2^* = w_{ESC}$ for $S_1 = S_{BKD}$ and $S_2 = S_{ESC}$ as follows:
# $$
# w_{1}^* S_{1}[0] - w_{2}^* S_{2}[0] = 0
# $$
# with another arbitrary linear constraint
# $$w_1^* - w_2^* = 1.$$
# So that it has value $0$ initially.
# Hence
# $$
# w_1^* = -\frac{S_2[0]}{S_1[0]-S_2[0]}, \quad
# w_2^* = -\frac{S_1[0]}{S_1[0]-S_2[0]}.
# $$
# Then we normalize them so that
# $$
# w_1 = \frac{w_1^*}{w_1^* + w_2^*}, \quad
# w_2 = \frac{w_2^*}{w_1^* + w_2^*}
# $$


# 1. Calculating weights
w1_star = -prices_test['ESC'][0] / (prices_test['BKD'][0] - prices_test['ESC'][0])
w2_star = w1_star - 1

w1 = w1_star / (w1_star + w2_star)
w2 = w2_star / (w1_star + w2_star)

print('Unnormalized weight: \n\
w1_star={}, \nw2_star={},\n\
Normalized weight:\n\
w1={} \nw2={}'.format(w1_star, w2_star, w1, w2))


# 2. Calculating Portfolio Series and daily P&L
portfolio_prices = w1 * prices_test['BKD'] - w2 * prices_test['ESC']
portfolio_pnl = np.diff(portfolio_prices, prepend=0)

# 3. Plotting portfolio prices
fig, ax = plt.subplots(figsize=(10,3), dpi=150)
ax.plot(portfolio_prices)
ax.title.set_text('Unit Portfolio Value for Pair ("BKD", "ESC") Calcualted From Price Series')
ax.grid()
fig.autofmt_xdate()
plt.show()

# 4. Calculating strategy daily P&L
pnl_gauss = portfolio_pnl * positions_gauss.values.T
equity_gauss = pnl_gauss.cumsum()

fig, ax = plt.subplots(figsize=(10,3), dpi=150)
ax.plot(equity_gauss, '--', color='g',label=r'Gauss AND')
ax.title.set_text('Strategy Performance on Unit Portfolio Calcualted From Daily P&L')
ax.grid()
fig.autofmt_xdate()
ax.legend()
plt.show()


# ### 4. Possible Issues Discussion
#
# #### Data Processing
# Log prices or CLR are not fundamentally stationary, and especially in real data, the training period may differ significantly from the testing period, rendering testing period data out of range.
# One may consider other alternatives.
#
# #### Copula Fitting
# The fitting results are very sensitive to the inputs.
# And more often than not, the fit score among copulas are not very different from each other.
# In some cases, one should look at the few best-suited copulas as candidates, instead of using a single copula.
#
# #### Copula Modeling
# Modeling and trading a pair of stocks' movements using copula, as implemented in the module, treats each stocks time series data as a random variable with stationary distribution.
# Though mathematically valid, this approach does not take into account each random variable as a time series, and re-shuffle the training data will yield the exact same result in terms of  fitted copula parameters and thus recommended positions.
# However, when compared to a vanilla Euclidean distance approach, this is one step further.
#
# Moreover, all the commonly used copulas are either Archimedean (Gumbel, Frank, etc.) or Elliptic (Student-t, Gaussian), which share some nice properties such as symmetry.
# However, the best-suited copula behind a pair of stocks may not necessarily be symmetric.


# ## Conclusion
# (This section follows from [Liew et al. 2013])<br>
# Copula introduces delicate assumptions on the exact coupled structure, along with other nice properties, of two random variables.
# In the pairs trading context, two stocks time series.
#
# * When compared to the Euclidean distance or cointegration approach, copula does not rely on assumptions of linear association or correlation coefficients as a measure of dependency.
#
# * Copula-based approach results in a far richer set of information, such as the shape and nature of the dependency between the stock pairs, thereby leading to potentially more robust modeling of the pair.
#
# * Some copula choices measure well with upper and lower tail dependencies of different extent, in an environment that considers both linear and non-linear relationship. 
#
# * Copulas possess an attractive property of being invariant under strictly monotone transformations of random variables. In other words, the same copula will be obtained regardless of whether the analyst is using price series or log price series.


# ## References ##
# - [Liew, R.Q. and Wu, Y., 2013. Pairs trading: A copula approach. Journal of Derivatives & Hedge Funds, 19(1), pp.12-30.](https://link.springer.com/article/10.1057/jdhf.2013.1)
# - [Stander, Y., Marais, D. and Botha, I., 2013. Trading strategies with copulas. Journal of Economic and Financial Sciences, 6(1), pp.83-107.](https://www.researchgate.net/publication/318054326_Trading_strategies_with_copulas)

