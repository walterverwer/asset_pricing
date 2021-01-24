# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:14:05 2021

@author: walte
"""

import yfinance as yf
import datetime
import pandas as pd

# constants:
stocks = ['^DJI', 'GS', 'MCD', 'DOW', 'CAT', 'MRK', 'CVX', 'VZ', 
          'MSFT', 'AMGN', 'CSCO', 'BA', 'PG', 'JPM', 'WBA', 'DIS',
          'KO', 'MMM', 'AXP', 'WMT', 'JNJ', 'HON', 'V', 'NKE',
          'AAPL', 'CRM', 'HD', 'TRV', 'UNH', 'INTC', 'IBM']
start_data = '2019-03-20' # important: stock 'DOW' is observed from this date onwards
end_data = '2020-12-31'

# get all stocks:
counter = 0
for stock in stocks:
    if counter == 0:
        df = pd.DataFrame(yf.download(stock, start=start_data, end=end_data)['Adj Close'])
        df[stock] = df['Adj Close']
        df.drop('Adj Close', inplace=True, axis = 1)
    else:
        df[stock] = yf.download(stock, start=start_data, end=end_data)['Adj Close']
    counter += 1
    

