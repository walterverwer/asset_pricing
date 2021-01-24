# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:14:05 2021

@author: walte
"""

# source: https://github.com/walterverwer/asset_pricing

import yfinance as yf
import pandas as pd
import os.path

# constants:
stocks = ['^DJI', 'GS', 'MCD', 'DOW', 'CAT', 'MRK', 'CVX', 'VZ', 
          'MSFT', 'AMGN', 'CSCO', 'BA', 'PG', 'JPM', 'WBA', 'DIS',
          'KO', 'MMM', 'AXP', 'WMT', 'JNJ', 'HON', 'V', 'NKE',
          'AAPL', 'CRM', 'HD', 'TRV', 'UNH', 'INTC', 'IBM']
start_data = '2019-03-21' # important: stock 'DOW' is observed from this date onwards
end_data = '2020-12-31'

if os.path.isfile('dow_jones_stocks.csv'): # check if data exists:
    df = pd.read_csv('dow_jones_stocks.csv')
    
else: # get all stocks using yahoo finance api:
    counter = 0 # used to handle the first stock in the list
    for stock in stocks:
        if counter == 0:
            df = pd.DataFrame(yf.download(stock, start=start_data, end=end_data)['Adj Close'])
            df[stock] = df['Adj Close']
            df.drop('Adj Close', inplace=True, axis = 1)
        else:
            df[stock] = yf.download(stock, start=start_data, end=end_data)['Adj Close']
        counter += 1 
    # save to csv:
    df.to_csv('dow_jones_stocks.csv')
    

