# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:14:05 2021

@author: walte
"""
## Question 2:

# source: https://github.com/walterverwer/asset_pricing

import yfinance as yf
import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
import os.path

# constants:
stocks = ['^DJI', 'GS', 'MCD', 'DOW', 'CAT', 'MRK', 'CVX', 'VZ', 
          'MSFT', 'AMGN', 'CSCO', 'BA', 'PG', 'JPM', 'WBA', 'DIS',
          'KO', 'MMM', 'AXP', 'WMT', 'JNJ', 'HON', 'V', 'NKE',
          'AAPL', 'CRM', 'HD', 'TRV', 'UNH', 'INTC', 'IBM']
start_data = '2019-03-21' # important: stock 'DOW' is observed from this date onwards
end_data = '2020-12-31'

if os.path.isfile('dow_jones_stocks.csv'): # check if data exists:
    df_prices = pd.read_csv('dow_jones_stocks.csv')
    
else: # get all stocks using yahoo finance api:
    counter = 0 # used to handle the first stock in the list
    for stock in stocks:
        if counter == 0:
            df_prices = pd.DataFrame(yf.download(stock, start=start_data, end=end_data)['Adj Close'])
            df_prices[stock] = df_prices['Adj Close']
            df_prices.drop('Adj Close', inplace=True, axis = 1)
        else:
            df_prices[stock] = yf.download(stock, start=start_data, end=end_data)['Adj Close']
        counter += 1 
    # set index date collumn:
    df_prices.set_index('Date')
    # save to csv:
    df_prices.to_csv('dow_jones_stocks.csv')

# construct return dataset:
df_returns = pd.DataFrame(index=df_prices.index)
for stock in stocks:
    df_returns[stock] = df_prices[stock].pct_change()

# drop na from calculating percent changes:
df_returns.dropna(inplace=True)

# compute mean and covvariance vector /matrix:
series_mean = df_returns.mean()
df_cov = df_returns.cov()

# construct parameters for A, B, C, and D:
n = len(series_mean) # just get n=31
Sigma_inv = inv(df_cov)
jota = np.ones(n)
mu = series_mean

# construct the A, B, C, and D definitions:
A = jota.T @ Sigma_inv @ mu     # jota' * Sigma^-1 * mu
B = mu.T @ Sigma_inv @ mu       # mu' * Sigma^-1 * mu
C = jota.T @ Sigma_inv @ jota   # jota' * Sigma^-1 * jota
D = B*C - A^2















