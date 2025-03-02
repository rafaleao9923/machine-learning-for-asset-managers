# Generated from: YFinance_Tutorial.ipynb
# Warning: This is an auto-generated file. Changes may be overwritten.

# # YFinance Tutorial: Pulling Free Financial Data
#
# yfinance is a popular Python library that offers a reliable, fast, and easy way to fetch historical market data from Yahoo Finance. Whether you're a seasoned data analyst, a budding quant trader, or a finance enthusiast, yfinance is a tool you'll find indispensable. In this tutorial, we'll walk through the basics of using yfinance to pull financial data.
#
# ## Documentation
# You can find the online documentation for `yfinance` here: https://python-yahoofinance.readthedocs.io/en/latest/
#
# ## Setting Up
#
# Ensure you have `yfinance` installed. If not, install it using pip, inside a notebook cell:
#
# ```python
# !pip install yfinance
# ```
#
# * If you are installing from the terminal, use: `pip install yfinance`.
# * If you followed the getting_started instructions, your python environment will already have it installed.


# ---
# ## Basic Usage of yfinance
# ### Importing the library
#
# After installation, you can import yfinance in your Python script or notebook:


import yfinance as yf


# ### Getting Historical Data
#
# To fetch historical market data for a specific stock, use the yf.Ticker class. For example, let's fetch data for Apple Inc:


apple = yf.Ticker("AAPL")
apple


# * You can get the historical market data using the history method. By default, it retrieves the last five days of stock data.
# * We will now reference the object `apple` when extracting data.


# Get the last 5 days of historical data
hist = apple.history(period="5d")
hist

# Fetching Real-Time Data
# Note: Real-time data might be delayed due to limitations from Yahoo Finance


# * To fetch data for a specific period, you can specify the period or start and end dates:


# Data for a specific period
hist_1m = apple.history(period="1mo")  # 1 month
hist_1year = apple.history(start="2020-01-01", end="2021-01-01")  # Specific date range, for each day

print('History: Monthly')
hist_1m.tail()


print('History: Year - each day')
hist_1year


# ### Adjusting for Stock Splits
# yfinance automatically adjusts historical data for stock splits. If you prefer unadjusted data, set auto_adjust to False:


hist_unadj = apple.history(period="1mo", auto_adjust=False)
hist_unadj


# ### Including Dividends and Stock Splits
# To include dividend and stock split data, set actions to True:


hist_adj = apple.history(period="5y", actions=True)
hist_adj


# ---
# ## Advanced Usage
#
# ### Fetching Data for Multiple Stocks
#
# To fetch data for multiple stocks, pass a list of ticker symbols to yf.download:


data = yf.download("AAPL MSFT GOOG", start="2020-01-01", end="2021-01-01")
data


# ### Fetching Real-Time Data
# For real-time data, you can use the interval parameter with the history method. For example, fetching minute-level data for the past 5 days:


real_time_data = apple.history(period="5d", interval="1m")
real_time_data


# **Note:**
# * Real-time data might be delayed by up to 15 minutes due to Yahoo Finance’s limitations.


# ---
# ## Conclusion
# yfinance is a powerful tool that provides easy access to a wealth of financial data. By integrating yfinance into your analysis, you gain the ability to make more informed decisions based on historical and real-time market data. Happy data hunting.

