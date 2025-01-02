# Data Preparation Tutorial¶

Get full version of MlFinLab

  

Note

This module was built with a research environment in mind. Meaning that it
assumes you are using historical data and testing different data structures.

This module doesn’t support real time data feeds, this was a design choice as
each user is likely to have their own database schemas and APIs.

First import your tick data.

    
    
    # Required Imports
    import numpy as np
    import pandas as pd
    
    data = pd.read_csv('data.csv')
    

In order to utilize the bar sampling methods presented below, our data must
first be formatted properly. Many data vendors will let you choose the format
of your raw tick data files. We want to only focus on the following 3 columns:
date_time, price, volume. The reason for this is to minimise the size of the
csv files and the amount of time when reading in the files.

Our data is sourced from TickData LLC which provides software called
TickWrite, to aid in the formatting of saved files. This allows us to save csv
files in the format date_time, price, volume. (If you don’t use TickWrite then
make sure to pre-format your files)

For this tutorial we will assume that you need to first do some pre-processing
and then save your data to a csv file.

    
    
    # Don't convert to datetime here, it will take forever to convert
    # on account of the sheer size of tick data files
    date_time = data['Date'] + ' ' + data['Time']
    new_data = pd.concat([date_time, data['Price'], data['Volume']], axis=1)
    new_data.columns = ['date', 'price', 'volume']
    

Initially, your instinct may be to pass an in-memory DataFrame object but the
truth is when you’re running the function in production, your raw tick data
csv files will be way too large to hold in memory. We used the subset 2011 to
2019 and it was more than 25 gigs. It is for this reason that the MlFinLab
package suggests using a file path to read the raw data files from disk.

Needless to say, there are times where an in-memory DataFrame is better, and
the functionality for this does exist.

    
    
    # Save to csv
    new_data.to_csv('FILE_PATH', index=False)
    

