# Generated from: Copula_Strategy_Mispricing_Index.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Copula Strategy Using Mispricing Index
# This notebook demonstrates the usage of the `copula_strategy_mpi` module.
# The framework of which was originally proposed in
#
# * Xie, W., Liew, R.Q., Wu, Y. and Zou, X., 2016. Pairs trading with copulas. 
#
# For a fundamental introduction of concepts in copula, please refer to the documentation for this module, or the basic copula strategy notebook.
# The rest of the notebook is written assuming the reader in possession of basic understanding of those concepts.
#
# **Warning:**
# The authors claimed a relatively robust 8-10% returns from this strategy in the formation period (6 mo).
# We are pretty positive that the rules proposed in the paper were implemented correctly in the `CopulaStrategyMPI`
# module with thorough unit testing on every possible case, and thus there is very unlikely to have mistakes.
# However the P&L is very sensitive to the opening and exiting parameters value, input data and copula choice,
# and it cannot lead to the claimed returns, after trying all the possible interpretations of ambiguities.
#
# We still implement this module for people who intend to explore possibilities with copula methods, however the user should be
# aware of the nature of the proposed framework.
# Interested reader may read through the *Possible Issues Discussion* part and see where this strategy can be improved.
# We also marked in the source code where the trading logics are implemented for you to change them quickly as you wish.


# ## Introduction to the Strategy Framework
# For convenience, the **mispricing index** implemented in the strategy will be referred to as **MPI** when no ambiguity arises.


# ### How is the MPI Strategy Constructed?
# At first glance, the MPI strategy documented in [Xie et al. 2016] looks quite bizarre.
# However, it is reasonably consistent when one goes through the logic of its construction:
# In order to use returns to generate trading signals, one needs to be creative about utilizing the information.
# It is one thing to know the dependence structure of a pair of stocks, it is another thing to trade based on it because intrinsically stocks are traded on prices, not returns.
#
# If one takes conditional probabilities as a distance measure on the spread, then it is natural to think about how far the returns can cumulatively drive the prices apart (or together), thereby introducing trading opportunities.
#
# Hence we introduce the following concepts for the strategy framework:
#
# #### Mispricing Index
# **MPI** is defined as the conditional probability (cumulative density) of returns, i.e., 
# $$
# MI_t^{X\mid Y} = P(R_t^X < r_t^X \mid R_t^Y = r_t^Y)
# $$
# $$
# MI_t^{Y\mid X} = P(R_t^Y < r_t^Y \mid R_t^X = r_t^X)
# $$
# for stocks $(X, Y)$ with returns random variables at day $t$: $(R_t^X, R_t^Y)$ and returns value at day $t$: $(r_t^X, r_t^Y)$.
# Those two values determine how mispriced each stock is, based on that day's return.
# Note that so far only one day's return information contributes, and we want to add it up to cumulatively use returns to gauge how mispriced the stocks are.
# Therefore we introduce the **flag** series:
#
# #### Flag and Raw Flag
# A more descriptive name than flag, in my opinion, would be the **cumulative mispricing index**.
# The **raw flag** series (with a star) is the cumulative sum of daily MPIs minus 0.5, i.e.,
# $$
# FlagX^*(t) = FlagX^*(t-1) + (MI_t^{X\mid Y} - 0.5), \quad FlagX^*(0) = 0.
# $$
# $$
# FlagY^*(t) = FlagY^*(t-1) + (MI_t^{Y\mid X} - 0.5), \quad FlagY^*(0) = 0.
# $$
# Or equivalently
# $$
# FlagX^*(t) = \sum_{s=0}^t (MI_s^{X\mid Y} - 0.5)
# $$
# $$
# FlagY^*(t) = \sum_{s=0}^t (MI_s^{Y\mid X} - 0.5)
# $$
# If one plots the raw flags series, they look quite similar to cumulative returns from their price series, which is what they were designed to do:
# Accumulate information from daily returns to reflect information on prices.
# Therefore, you may consider it as a fancy way to represent the returns series.
#
# However, the **real flag** series (without a star, $FlagX(t), FlagY(t)$) **will be reset to $0$** whenever there is an exiting signal, which brings us to the trading logic.


# ### Trading Logic
#
# The authors propose a **dollar-neutral** trade scheme worded as follows:
#
# Suppose stock $X$, $Y$ are associated with $FlagX$, $FlagY$ respectively.
#
# Opening rules: ($D = 0.6$ in the paper)
# * When $FlagX$ reaches $D$, we short-sell stock $X$ and buy stock $Y$ in **equal amounts**. ($-1$ Position)
# * When $FlagX$ reaches $-D$, we short-sell stock $Y$ and buy stock $X$ in **equal amounts**. ($1$ Position)
# * When $FlagY$ reaches $D$, we short-sell stock $Y$ and buy stock $X$ in **equal amounts**. ($1$ Position)
# * When $FlagY$ reaches $-D$, we short-sell stock $X$ and buy stock $Y$ in **equal amounts**. ($-1$ Position)
#
# Exiting rules: ($S = 2$ in the paper)
# * If trades are opened based on $FlagX$, then they are closed if $FlagX$ returns to zero or reaches stop-loss position $S$ or $-S$.
#
# * If trades are opened based on $FlagY$, then they are closed if $FlagY$ returns to zero or reaches stop-loss position $S$ or $-S$.
#
# * After trades are closed, both $FlagX$ and $FlagY$ are reset to $0$.
#
# The rationale behind the dollar-neutral choice might be that (the authors did not mention this), because the signals are generated by returns, it makes sense to "reset" returns when entering into a long/short position.


# #### Ambiguities
# The authors did not specify what will happen if the followings occur:
#
# 1. When $FlagX$ reaches $D$ (or $-D$) and $FlagY$ reaches $D$ (or $-D$) together.
# 2. When in a long(or short) position, receives a short(or long) trigger.
# 3. When receiving an opening and exiting signal together.
# 4. When the position was open based on $FlagX$ (or $FlagY$), $FlagY$ (or $FlagX$) reaches $S$ or $-S$.
#
# Here is our take on the above issues:
#
# 1. Do nothing.
# 2. Change to the trigger position. For example, long position with a short trigger will go short.
# 3. Go for the exiting signal.
# 4. Do nothing.


# #### Choices for Open and Exit Logic
#
# The above default logic is essentially an OR-OR logic for open and exit: When at least one of the 4 open conditions is satisfied, an
# open signal (long or short) is triggered;
# Similarly for the exit logic, to exit only one of them needs to be satisfied.
# The opening trigger is in general too sensitive and leads to too many trades, and [Rad et al. 2016] suggested using AND-OR logic instead.
# Thus, to achieve more flexibility, we allow the user to choose AND, OR for both open and exit logic and hence there are 4 possible combinations.
# Based on our tests we found AND-OR to be the most reasonable choice in general, but in certain situations other choices may have an edge.
#
# The default is OR-OR, as suggested in [Xie et al. 2014], and you can switch to other logic in the `get_positions_and_flags` method
# by setting `open_rule` and `exit_rule` to your own liking.
# For instance `open_rule='and'`, `exit_rule='or'`.


# ## `CopulaStrategyMPI` Functionality ##
# Tools included in the module enables the users to conduct the following workflow:
#
# * Initiate the `CopulaStrategyMPI` class with options to set custom $D$ value `opening_triggers` and $S$ value `stop_loss_positions`, and the option to side-load a fitted `Copula` or `MixedCopula` object.
# * Calculate returns from price series using `to_returns` method.
# * Calculate daily MPIs from returns using `calc_mpi` method.
#   (This step is optional and you do not need the MPI series to do other things.
#   Other methods that uses MPIs will calculate them internally.)
# * Fit returns to different kinds of copulas using `fit_copula` method.
# * Get positions and flags from testing/trading data, using `get_positions_and_flags` method.
# * Translate positions to the number of units to hold for a dollar-neutral approach, using `positions_to_units_dollar_neutral` method.
#
# A few notes:
#
# 1. This module is pandas based, and is built on top of the `BasicCopulaStrategy` class.
# 2. The output is *very sensitive* to the values of `opening_triggers` and `stop_loss_positions`, to the point that it may determine whether this strategy profits or loses.
# 3. If you just want to have the raw flag series, simply toggle `enable_reset_flag` to `False`. But this logically conflicts with the exiting logic generation so do not use the trading signal under this condition.
# 4. If you want to have the raw flag series AND trade on it, you need to set `stop_loss_positions` to `(-np.inf, np.inf)` and toggle `enable_reset_flag` to `False`. Although based on our tests, this strategy is not likely to profit.


# ## Usage ##
# The demonstration part has the following sections using real-world data:
# 1. Importing and Data Pre-processing.
# 2. Fitting Data to Different Copulas with Training Data.
# 3. Generating Trading Positions using Testing Data.
# 4. Possible Issues Discussion.


# ### 1. Importing and Data Preprocessing
#
# I have also included the 2009-2011 data for BKD and ESC. Simply uncomment accordingly for cell 2, 3 and 4.


# Importing libraries and modules
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import statsmodels.api as sm

from arbitragelab.trading import MPICopulaTradingRule
import arbitragelab.copula_approach.copula_calculation as ccalc
from arbitragelab.copula_approach.archimedean import (Gumbel, Clayton, Frank, Joe, N13, N14)
from arbitragelab.copula_approach.elliptical import (StudentCopula, GaussianCopula)


# Importing data

# I also included the 2009-2011 data. Uncomment below to use.
# pair_prices = pd.read_csv(r'BKD_ESC_2009_2011.csv', index_col=0, parse_dates=True)

pair_prices = pd.read_csv(r'BKD_ESC_2008_2009_June.csv', index_col=0, parse_dates=True)


# Plotting price series
plt.figure(dpi=120)
plt.plot(pair_prices['BKD'], label='BKD')
plt.plot(pair_prices['ESC'], label='ESC')

# plt.axvline(dt.date(2012, 1, 3), color='red')  # Training testing split date

plt.axvline(dt.date(2008, 12, 31), color='red')  # Training testing split date
plt.legend()
plt.grid()
plt.gcf().autofmt_xdate()
plt.title(r'Original Price Series of BKD and ESC')
plt.show()


# Initiate the analysis module
CSMPI = MPICopulaTradingRule()

# Training and testing split. Note that this module works with returns series.
# training_length = 756# From 01/02/2008 to 12/30/2008 (m/d/y)
training_length = 252 # From 01/02/2008 to 12/30/2008 (m/d/y)

prices_train = pair_prices.iloc[: training_length, :]
returns_train = CSMPI.to_returns(prices_train)

prices_test = pair_prices.iloc[training_length : , :]
returns_test = CSMPI.to_returns(prices_test)

# Empirical CDF for the training set.
cdf1 = ccalc.construct_ecdf_lin(returns_train['BKD'])
cdf2 = ccalc.construct_ecdf_lin(returns_train['ESC'])

cdf1_price = ccalc.construct_ecdf_lin(prices_train['BKD'])
cdf2_price = ccalc.construct_ecdf_lin(prices_train['ESC'])


# Let's at first scatter plot the training data to have a grasp on its dependence structure, and determine which copula it should fit.


# Scatter plot the training data.
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,5), dpi=100)
axs[0].scatter(cdf1(returns_train['BKD']), cdf2(returns_train['ESC']), s=2)
axs[0].set_aspect('equal', adjustable='box')
axs[0].set_title(r'From Return Series, Training Data')

axs[1].scatter(cdf1_price(prices_train['BKD']), cdf2_price(prices_train['ESC']), s=2, color='r')
axs[1].set_aspect('equal', adjustable='box')
axs[1].set_title(r'From Price Series, Training Data')
plt.tight_layout()
plt.show()


# **Note: We only use the returns series for the MPI strategy. The price series scatter plot is just for visual comparison.**
#
# The returns plot exhibits some tail dependencies on the lower-left corner.
# There might also be some tail dependencies on the upper-right corner, but it is not directly obvious.
# When compared to the price series scatter plot, the price series shows a much stronger lower dependency and no clear upper dependency.
# In terms of market movement, the two plots indicate that both returns and prices tend to move downward together, but not upward together, at least the interdependence is not as strong as downward movements.
# Considering the training data is in year 2008, those scatter plots make sense.
#
# ### 2. Fitting Data to Different Copulas with Training Data
#
# Regarding which copulas best describe the structure, we propose using N14 copula log-likelihood score, and their ability to capture tail dependencies at both corners.
# One may fit to as much the copulas as they wish in the `copula_approach` package.


# Fit to Gumbel, Frank, Clayton, Joe, N14, Gaussian and Student-t copulas respectively, and print the scores.
# You may see warnings coming from fitting a mixed copula. In this case, adjust values for gamma_scad, a_scad.
fit_result_gumbel, copula_gumbel, cdf_x_gumbel, cdf_y_gumbel =\
    ccalc.fit_copula_to_empirical_data(x=returns_train['BKD'], y=returns_train['ESC'], copula=Gumbel)

fit_result_frank, copula_frank, cdf_x_frank, cdf_y_frank =\
    ccalc.fit_copula_to_empirical_data(x=returns_train['BKD'], y=returns_train['ESC'], copula=Frank)

fit_result_clayton, copula_clayton, cdf_x_clayton, cdf_y_clayton =\
    ccalc.fit_copula_to_empirical_data(x=returns_train['BKD'], y=returns_train['ESC'], copula=Clayton)

fit_result_joe, copula_joe, cdf_x_joe, cdf_x_joe=\
    ccalc.fit_copula_to_empirical_data(x=returns_train['BKD'], y=returns_train['ESC'], copula=Joe)

fit_result_n14, copula_n14, cdf_x_n14, cdf_y_n14=\
    ccalc.fit_copula_to_empirical_data(x=returns_train['BKD'], y=returns_train['ESC'], copula=N14)

fit_result_gauss, copula_gauss, cdf_x_gauss, cdf_y_gauss =\
    ccalc.fit_copula_to_empirical_data(x=returns_train['BKD'], y=returns_train['ESC'], copula=GaussianCopula)

fit_result_t, copula_t, cdf_x_t, cdf_y_t=\
    ccalc.fit_copula_to_empirical_data(x=returns_train['BKD'], y=returns_train['ESC'], copula=StudentCopula)

# Print fit scores
print(fit_result_gumbel)
print(fit_result_frank)
print(fit_result_clayton)
print(fit_result_joe)
print(fit_result_n14)
print(fit_result_gauss)
print(fit_result_t)


# Note that we are working with the returns series, which in general is much noisier than price series, and has a lower level of correlation.


# Plotting copulas
fig, ax = plt.subplots(figsize=(5,7), dpi=100)

ax.scatter(cdf1(returns_train['BKD']), cdf2(returns_train['ESC']), s=1)
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'BKD and ESC Returns Series, Training Data')
ax.set_xlim([-0.05, 1.05])
ax.set_ylim([-0.05, 1.05])
plt.tight_layout()

plt.show()


# Gumbel
copula_gumbel.plot_scatter(num_points=training_length);


# Frank
copula_frank.plot_scatter(num_points=training_length);


# Clayton
copula_clayton.plot_scatter(num_points=training_length);


# Joe
copula_joe.plot_scatter(num_points=training_length);


# N14
copula_n14.plot_scatter(num_points=training_length);


# Gaussian
copula_gauss.plot_scatter(num_points=training_length);


# Student-t
copula_t.plot_scatter(num_points=training_length);


# Now we choose Student-t and N14 copula to generate trading signals.
#
# ### 3. Generating Trading Positions using Testing Data
#
# We are using a dollar neutral strategy, and the buy/sell/hold is based on "flag" series, calculated from accumulations of mispricing indices.
# For more detail, please refer to the beginning of the notebook.
#
# Here we use the default OR-OR open-exit logic with the Student-t copula, and AND-OR open-exit logic with the
# N14 copula.


# Make two strategy classes with the fitted Student and N14 copula.
CSMPI_t = MPICopulaTradingRule(opening_triggers=(-0.2, 0.2), stop_loss_positions=(-2, 2))
CSMPI_t.set_copula(copula_t)
CSMPI_t.set_cdf(cdf_x_t, cdf_y_t)

CSMPI_n14 = MPICopulaTradingRule(opening_triggers=(-0.5, 0.5), stop_loss_positions=(-2.1, 2.1))
CSMPI_n14.set_copula(copula_n14)
CSMPI_n14.set_cdf(cdf_x_n14, cdf_y_n14)

# Get positions and flag series
positions_t, flags_t = CSMPI_t.get_positions_and_flags(
    returns=returns_test, enable_reset_flag=True)
positions_n14, flags_n14 = CSMPI_n14.get_positions_and_flags(
    returns=returns_test, enable_reset_flag=True,
    open_rule='and', exit_rule='or')

# Shift the positions by 1 day
positions_t = positions_t.shift(1)
positions_n14 = positions_n14.shift(1)
positions_t[0] = 0
positions_n14[0] = 0


# As a referece we also plot the normalized price series from the two stocks.
plt.figure(figsize=(10, 3), dpi=150)
plt.plot(prices_test['BKD'] / prices_test['BKD'][0], label='BKD prices')
plt.plot(prices_test['ESC'] / prices_test['ESC'][0], label='ESC prices')
plt.title('Normalized Prices in the Trading Period')
plt.legend()
plt.grid()
plt.show()

# Plot positions and flags
fig, axs = plt.subplots(4, 1, gridspec_kw={'height_ratios': [1, 0.4, 1, 0.4]}, figsize=(10,10), dpi=150)
fig.suptitle('Flags and Corresponding Positions')

# Plotting flags for Student-t copula
axs[0].plot(flags_t['BKD'], label='BKD')
axs[0].plot(flags_t['ESC'], label='ESC')
axs[0].title.set_text('Flags, Student-t Copula')
axs[0].legend()
axs[0].grid()
axs[0].set_yticks([-2, -1, -0.6, 0, 0.6, 1, 2])

# Plotting positions for Student-t copula
axs[1].plot(positions_t, label='Positions', color='brown')
axs[1].title.set_text('Positions, Student-t Copula')
axs[1].grid()
axs[1].set_yticks([-1,0,1])

# Plotting flags for N14 copula
axs[2].plot(flags_n14['BKD'], label='BKD')
axs[2].plot(flags_n14['ESC'], label='ESC')
axs[2].title.set_text('Flags, N14 Copula')
axs[2].legend()
axs[2].grid()
axs[2].set_yticks([-2, -1, -0.6, 0, 0.6, 1, 2])

# Plotting positions for N14 copula
axs[3].plot(positions_n14, label='Positions', color='brown')
axs[3].title.set_text('Positions, N14 Copula')
axs[3].grid()
axs[3].set_yticks([-1,0,1])

fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Avoid title overlap
plt.show()


# #### Forming Equity Curves
# The authors propose a dollar-neutral trading strategy and therefore, we can represent the P&L of the strategy in returns.


# 1. Calculate the unit holding series
units_df_t = CSMPI.positions_to_units_dollar_neutral(prices_df=prices_test, positions=positions_t)
units_df_n14 = CSMPI.positions_to_units_dollar_neutral(prices_df=prices_test, positions=positions_n14)

# Calculate returns from the strategy, i.e., assuming 1$ initial investment and calculate P&L.
# 2. Calculate Daily P&L of the strategy based on the units holding for each security
portfolio_pnl_t = returns_test['BKD'] * units_df_t['BKD'] + returns_test['ESC'] * units_df_t['ESC']
portfolio_pnl_n14 = returns_test['BKD'] * units_df_n14['BKD'] + returns_test['ESC'] * units_df_n14['ESC']

# 3. Calculate and plot the equity curve
equity_t = portfolio_pnl_t.cumsum()
equity_n14 = portfolio_pnl_n14.cumsum()

# Plotting
fig, axs = plt.subplots(4, 1, gridspec_kw={'height_ratios': [0.5, 0.2, 0.2, 0.5]}, figsize=(10,10), dpi=150)

# As a referece we also plot the normalized price series from the two stocks.
axs[0].plot(prices_test['BKD'] / prices_test['BKD'][0], label='BKD prices')
axs[0].plot(prices_test['ESC'] / prices_test['ESC'][0], label='ESC prices')
axs[0].set_title('Normalized Prices in the Trading Period')
axs[0].legend()
axs[0].grid()

# Plot the units series
axs[1].plot(units_df_t['BKD'], label='BKD units')
axs[1].plot(units_df_t['ESC'], label='ESC units')
axs[1].set_title('Amount of Shares to Hold According to Student-t Copula')
axs[1].legend()
axs[1].grid()

axs[2].plot(units_df_n14['BKD'], label='BKD units')
axs[2].plot(units_df_n14['ESC'], label='ESC units')
axs[2].set_title('Amount of Shares to Hold According to N14 Copula')
axs[2].legend()
axs[2].grid()

# Plot the daily P&L
axs[3].plot(equity_t, label='Student-t', color='firebrick')
axs[3].plot(equity_n14, label='N14', color='forestgreen')
axs[3].set_title('Equity Curves, Plotted in Returns')
axs[3].legend()
axs[3].grid()

fig.tight_layout()
plt.show()


# ### 4. Possible Issues Discussion
# The following are critiques for the default strategy.
# For a thorough comparison in large amounts of stocks across several decades, read For the AND-OR strategy, read more 
# in [Rad et al. 2016] on comparisons with other common strategies, using the AND-OR logic.
#
# 1. The strategy's outcome is quite sensitive to the values of opening and exiting triggers to the point that a well-fitted copula with a not good sets of parameters can actually lose money.
#
# 2. The trading signal is generated from the flags series, and the flags series will be calculated from the copula that we use to model.
#    Therefore the explainability suffers.
#    Also, it is based on the model in second order, and therefore the flag series and the suggested positions will be quite different across different copulas, making it not stable and not directly comparable mutually.
#
# 3. The way the flags series are defined does not handle well when both stocks are underpriced/overpriced concurrently.
#
# 4. Because of flags will be reset to 0 once there is an exiting signal, it implicitly models the returns as martingales that do not depend on the current price level of the stock itself and the other stock.
#    Such an assumption may be situational, and the user should be aware. (White noise returns do not imply that the prices are well cointegrated.)
#
# 5. The strategy is betting the flags series having dominating mean-reversion behaviors, for a pair of cointegrated stocks.
#    It is not mathematically clear what justifies the rationale.
#
# 6. If accumulating mispricing index is basically using returns to reflect prices, and the raw flags look basically the same as normalized prices, why not just directly use normalized prices?


# ## Conclusion
#
# (This section follows from [Xie et al. 2016])
#
# * Copulas are able to capture both linear and non-linear relations between random variables, it is possible that the proposed method captures strong non-linear associations that the traditional methods such as distance measure tend to neglect.
#
# * Using returns overcomes the criticism that the prices series not being stationary, as used by [Liew et al. 2013].


# ## References ##
# - [Xie, W., Liew, R.Q., Wu, Y. and Zou, X., 2016. Pairs trading with copulas. The Journal of Trading, 11(3), pp.41-52.](https://efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2014-Rome/papers/EFMA2014_0222_FullPaper.pdf)
# - [Liew, R.Q. and Wu, Y., 2013. Pairs trading: A copula approach. Journal of Derivatives & Hedge Funds, 19(1), pp.12-30.](https://dr.ntu.edu.sg/bitstream/10220/17826/1/jdhf20131a.pdf)
# - [Rad, H., Low, R.K.Y. and Faff, R., 2016. The profitability of pairs trading strategies: distance, cointegration and copula methods. Quantitative Finance, 16(10), pp.1541-1558.](https://www.tandfonline.com/doi/pdf/10.1080/14697688.2016.1164337?casa_token=X0-FdUqDsv4AAAAA:ZFothfEHF-dO2-uDtFo2ZuFH0uzF6qijsweHD888yfPx3OZGXW6Szon1jvA2BB_AsgC5-kGYreA4fw)

