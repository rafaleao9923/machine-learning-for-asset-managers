# Generated from: futures_rollover.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # Futures Rolling
#
# ## Introduction to Futures
# Futures are a form of a contract drawn up between two parties to purchase or sell a quantity of an underlying asset at a specified date in the future. This date is known as the delivery or expiration. When this date is reached, the buyer must deliver the physical underlying (or cash equivalent) to the seller for the price agreed at the contract formation date.
#
# In practice, futures are traded on exchanges for standardised quantities and qualities of the underlying. The prices are marked to market every day. Futures are incredibly liquid and are used heavily for speculative purposes. While futures were often utilised to hedge the prices of agricultural or industrial goods, a futures contract can be formed on any tangible or intangible underlying such as stock indices, interest rates of foreign exchange values.
#
# The main difference between a futures contract and equity ownership is the fact that a futures contract has a limited window of availability by virtue of the expiration date. At any one instant, there will be a variety of futures contracts on the same underlying all with varying dates of expiry. The contract with the nearest date of expiry is known as the near contract.
#
# ## Outline
#
# - Contract Rollers
#     - [Crude Oil - WTI](#wti) 
#     - [UK Gas - NBP](#ukgas)
#     - [Gasoline - RBOB](#rbob)
#     - [Soybean - S](#soyb)
#     - [Soy Oil - B0](#soyo)
#     - [Corn - C](#corn)
#     - [Ethanol - EH](#eth)


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from arbitragelab.util.rollers import *

import warnings
warnings.filterwarnings('ignore')


# # Crude Oil WTI  <a class="anchor" id="wti"></a>
#
# NYMEX WTI Crude Oil futures (CL) is the world’s most liquid crude oil contract. When traders need the current oil price, they check the WTI Crude Oil price. WTI (West Texas Intermediate, a US light sweet crude oil blend) futures provide direct crude oil exposure and are the most efficient way to trade oil after a sharp rise in US crude oil production. They can also be used to hedge against adverse oil price moves or speculate on whether WTI oil prices will rise or fall.
#
# https://www.cmegroup.com/trading/energy/crude-oil/light-sweet-crude_contract_specifications.html
#
# ### Termination of Trading
#
# Trading terminates 3 business day prior to the 25th calendar day of the month prior to the contract month. If the 25th calendar day is not a business day, trading terminates 4 business days prior to the 25th calendar day of the month prior to the contract month.


# Load contract price data.
cl_df = pd.read_csv('./data/futures_price_data/CL1.csv')
cl_df['Dates'] = pd.to_datetime(cl_df['Dates'])
cl_df.dropna(inplace=True)
cl_df.index = cl_df['Dates']
cl_df = cl_df['2006-01': '2019-12']


# Fit corresponding roller and retrieve gaps.
wti_roller = CrudeOilFutureRoller().fit(cl_df)
wti_gaps = wti_roller.transform()


# Plot the Normal, Rolled and Gaps Series.
(cl_df['PX_LAST'] - wti_gaps).plot(figsize=(15,10))
cl_df['PX_LAST'].plot()
wti_gaps.plot()

plt.legend(["Rolled", "Normal", "Gaps"])
plt.title("WTI future rolling plot");


# Sometimes rolled contracts dip into negative territory. This
# can cause problems when used for ml models, thus there is the
# ability of using the parameter 'handle_negative_roll', which
# will process the price data into positive returns data.
non_negative_cl = wti_roller.transform(handle_negative_roll=True) 
non_negative_cl.to_csv('./data/nonneg_forward_rolled_futures/NonNegative_CL_forward_roll.csv')
non_negative_cl.plot(figsize=(15,10))
plt.title("WTI Non Negative Forward Roll");


# The diagnostic summary is a helper function to help the user
# easily double check expiration dates and their respective gap
# calculations.
wti_diag_frame = wti_roller.diagnostic_summary()
wti_diag_frame.head(10)


# # NBP UK Natural Gas Futures  <a class="anchor" id="nbp"></a>
#
# Natural gas is the third most important source of energy after oil and coal. The use of natural gas is growing quickly and is expected to overtake coal in the second spot by 2030.
#
# The world’s largest producers of natural gas are currently the United States, Russia, Iran, Qatar, Canada, China and Norway. These countries have excess natural gas that can be exported to other countries around the world, which is either transported through pipelines or as liquefied natural gas (LNG).
#
# In western Europe, gas is the dominant fuel for electricity production. Prices are set at several trading hubs around the region. The two most important hubs in the region are the National Balancing Point or NBP in the UK and the Title Transfer Facility or TTF in the Netherlands.
#
# https://www.theice.com/products/910/UK-Natural-Gas-Futures
#
# ## Termination of Trading
# Trading will cease at the close of business two Business Days prior to the first calendar day of the delivery month, quarter, season, or calendar.


# Load contract price data.
nbp_df = pd.read_csv('./data/futures_price_data/NBP1.csv')
nbp_df['Dates'] = pd.to_datetime(nbp_df['Dates'])
nbp_df.set_index('Dates', inplace=True)


# Fit corresponding roller and retrieve gaps.
nbp_roller = NBPFutureRoller().fit(nbp_df)
nbp_gaps = nbp_roller.transform()


# Plot the Normal, Rolled and Gaps Series.
(nbp_df['PX_LAST'] - nbp_gaps).plot(figsize=(15,10))
nbp_df['PX_LAST'].plot()
nbp_gaps.plot()

plt.legend(["Rolled", "Normal", "Gaps"])
plt.title("NBP future rolling plot");


# The diagnostic summary is a helper function to help the user
# easily double check expiration dates and their respective gap
# calculations.
nbp_diag_frame = nbp_roller.diagnostic_summary()
nbp_diag_frame.head(10)


# # RBOB  <a class="anchor" id="rbob"></a>
#
# RBOB products offer a way for investors to express views on crude oil, weather, consumer behavior and regulatory action in terms of current and future energy consumption. As the primary fuel for most automobiles on the road, gasoline is an integral commodity to the lives of most consumers. 
#
# https://www.cmegroup.com/trading/energy/refined-products/rbob-gasoline_contract_specifications.html
#
# ### Termination of Trading
# Trading terminates on the last business day of the month prior to the contract month.


# Load contract price data.
rb_df = pd.read_csv('./data/futures_price_data/RB1.csv').dropna()
rb_df['Dates'] = pd.to_datetime(rb_df['Dates'])
rb_df.set_index('Dates', inplace=True)
rb_df = rb_df['2006-01': '2019-12']


# Fit corresponding roller and retrieve gaps.
rbob_roller = RBFutureRoller().fit(rb_df)
rbob_gaps = rbob_roller.transform()


# Plot the Normal, Rolled and Gaps Series.
(rb_df['PX_LAST'] - rbob_gaps).plot(figsize=(15,10))
rb_df['PX_LAST'].plot()
rbob_gaps.plot()

plt.legend(["Rolled", "Normal", "Gaps"])
plt.title("RBOB future rolling plot");


# In this case the rolled contract dips into negative territory.
# Thus the 'handle_negative_roll' parameter is used to post process
# the rolled future data.
non_negative_rbob = rbob_roller.transform(handle_negative_roll=True)
non_negative_rbob.to_csv('./data/nonneg_forward_rolled_futures/NonNegative_RB_forward_roll.csv')
non_negative_rbob.plot(figsize=(15,10))
plt.title("RBOB Non Negative Forward Roll");


# The diagnostic summary is a helper function to help the user
# easily double check expiration dates and their respective gap
# calculations.
rb_diag_frame = rbob_roller.diagnostic_summary()
rb_diag_frame.head(10)


# # Soybeans S1  <a class="anchor" id="soyb"></a>
#
#
#
# ### Termination of Trading
# Trading terminates on the business day prior to the 15th day of the contract month.


# Load contract price data.
soybean_df = pd.read_csv('./data/futures_price_data/S1.csv', index_col='Date', parse_dates=True).dropna()
soybean_df = soybean_df['2006-01': '2019-12']


# Fit corresponding roller and retrieve gaps.
soy_roller = GrainFutureRoller().fit(soybean_df)
soy_gaps = soy_roller.transform()


# Plot the Normal, Rolled and Gaps Series.
(soybean_df['PX_LAST'] - soy_gaps).plot(figsize=(15,10))
soybean_df['PX_LAST'].plot()
soy_gaps.plot()

plt.legend(["Rolled", "Normal", "Gaps"])
plt.title("S future rolling plot");


# The diagnostic summary is a helper function to help the user
# easily double check expiration dates and their respective gap
# calculations.
soy_diag_frame = soy_roller.diagnostic_summary()
soy_diag_frame.head(10)


# Example on how to analyze and verify gaps using the backwardation/contango plot.

soybean_m1_df = pd.read_csv('./data/futures_price_data/S1.csv', index_col='Date', parse_dates=True).dropna()
soybean_m1_df = soybean_m1_df['2006-01': '2019-12']

soybean_m2_df = pd.read_csv('./data/futures_price_data/S2.csv', index_col='Date', parse_dates=True).dropna()
soybean_m2_df = soybean_m2_df['2006-01': '2019-12']

soy_gaps.plot(figsize=(15,5))
plt.title("Soybean Future Gaps");
plt.show()

plot_historical_future_slope_state(soybean_m1_df['PX_LAST'], soybean_m2_df['PX_OPEN'])
plt.title("Contango/Backwardation plot");


# # Soyoil B01  <a class="anchor" id="soyo"></a>
#
# RBOB products offer a way for investors to express views on crude oil, weather, consumer behavior and regulatory action in terms of current and future energy consumption. As the primary fuel for most automobiles on the road, gasoline is an integral commodity to the lives of most consumers. 
#
# https://www.cmegroup.com/trading/energy/refined-products/rbob-gasoline_contract_specifications.html
#
# ### Termination of Trading
# Trading terminates on the business day prior to the 15th day of the contract month.


# Load contract price data.
soyoil_df = pd.read_csv('./data/futures_price_data/B01.csv', index_col='Date', parse_dates=True).dropna()
soyoil_df = soyoil_df['2006-01': '2019-12']


# Fit corresponding roller and retrieve gaps.
soyo_roller = GrainFutureRoller().fit(soyoil_df*11)
soyo_gaps = soyo_roller.transform()


# Plot the Normal, Rolled and Gaps Series.
(soyoil_df['PX_LAST'] - soyo_gaps).plot(figsize=(15,10))
soyoil_df['PX_LAST'].plot()
soyo_gaps.plot()

plt.legend(["Rolled", "Normal", "Gaps"])
plt.title("B0 future rolling plot");


# The diagnostic summary is a helper function to help the user
# easily double check expiration dates and their respective gap
# calculations.
soyo_diag_frame = soyo_roller.diagnostic_summary()
soyo_diag_frame.head(10)


# Example on how to analyze and verify gaps using the backwardation/contango plot.

soyo_m1_df = pd.read_csv('./data/futures_price_data/B01.csv', index_col='Date', parse_dates=True).dropna()
soyo_m1_df = soyo_m1_df['2006-01': '2019-12']

soyo_m2_df = pd.read_csv('./data/futures_price_data/B02.csv', index_col='Date', parse_dates=True).dropna()
soyo_m2_df = soyo_m2_df['2006-01': '2019-12']

soyo_gaps.plot(figsize=(15,5))
plt.title("Soyoil Future Gaps");
plt.show()

plot_historical_future_slope_state(soyo_m1_df['PX_LAST'], soyo_m2_df['PX_OPEN'])
plt.title("Contango/Backwardation plot");


# # Corn C1  <a class="anchor" id="corn"></a>
#
#
# ### Termination of Trading
# Trading terminates on the business day prior to the 15th day of the contract month.


# Load contract price data.
corn_df = pd.read_csv('./data/futures_price_data/C1.csv', index_col='Date', parse_dates=True).dropna()
corn_df = corn_df['2006-01': '2019-12']


# Fit corresponding roller and retrieve gaps.
corn_roller = GrainFutureRoller().fit(corn_df)
corn_gaps = corn_roller.transform()


# Plot the Normal, Rolled and Gaps Series.
(corn_df['PX_LAST'] - corn_gaps).plot(figsize=(15,10))
corn_df['PX_LAST'].plot()
corn_gaps.plot()

plt.legend(["Rolled", "Normal", "Gaps"])
plt.title("Corn future rolling plot");


# The diagnostic summary is a helper function to help the user
# easily double check expiration dates and their respective gap
# calculations.
corn_diag_frame = corn_roller.diagnostic_summary()
corn_diag_frame.head(10)


# Example on how to analyze and verify gaps using the backwardation/contango plot.

corn_m1_df = pd.read_csv('./data/futures_price_data/C1.csv', index_col='Date', parse_dates=True).dropna()
corn_m1_df = corn_m1_df['2006-01': '2019-12']

corn_m2_df = pd.read_csv('./data/futures_price_data/C2.csv', index_col='Date', parse_dates=True).dropna()
corn_m2_df = corn_m2_df['2006-01': '2019-12']

corn_gaps.plot(figsize=(15,5))
plt.title("Corn Future Gaps");
plt.show()

plot_historical_future_slope_state(corn_m1_df['PX_LAST'], corn_m2_df['PX_OPEN'])
plt.title("Contango/Backwardation plot");


# # Ethanol EH1 <a class="anchor" id="corn"></a>
#
#
# ### Termination of Trading
# Trading terminates on 3rd business day of the contract month.


# Load contract price data.
ethanol_df = pd.read_csv('./data/futures_price_data/EH1.csv', index_col='Date', parse_dates=True).dropna()
ethanol_df = ethanol_df['2006-01': '2019-12']


# Fit corresponding roller and retrieve gaps.
ethanol_roller = EthanolFutureRoller().fit(ethanol_df)
ethanol_gaps = ethanol_roller.transform()


# Plot the Normal, Rolled and Gaps Series.
(ethanol_df['PX_LAST'] - ethanol_gaps).plot(figsize=(15,10))
ethanol_df['PX_LAST'].plot()
ethanol_gaps.plot()

plt.legend(["Rolled", "Normal", "Gaps"])
plt.title("Ethanol future rolling plot");


# Example on how to analyze and verify gaps using the backwardation/contango plot.

ethanol_m1_df = pd.read_csv('./data/futures_price_data/EH1.csv', index_col='Date', parse_dates=True).dropna()
ethanol_m1_df = ethanol_m1_df['2006-01': '2019-12']

ethanol_m2_df = pd.read_csv('./data/futures_price_data/EH2.csv', index_col='Date', parse_dates=True).dropna()
ethanol_m2_df = ethanol_m2_df['2006-01': '2019-12']

ethanol_gaps.plot(figsize=(15,5))
plt.title("Corn future rolling plot");
plt.show()

plot_historical_future_slope_state(ethanol_m1_df['PX_LAST'], ethanol_m2_df['PX_OPEN'])
plt.title("Contango/Backwardation plot");


# # Conclusion
#
# This notebook describes the methods used to roll futures for different assets. This is done to get a continuous price series for a given set of futures contracts.
#
# Types of contracts covered in this notebooks are:
# * Crude Oil - WTI
# * UK Gas - NBP
# * Gasoline - RBOB
# * Soybean - S
# * Soy Oil - B0
# * Corn - C
# * Ethanol - EH

