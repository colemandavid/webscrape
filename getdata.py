#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:05:13 2019

@author: colemanda
"""

# API details here:
# https://www.alphavantage.co/documentation/#dailyadj

# Need 2 different things:
# Go get initial stock data for all stocks in the:
# S&P 500
# Russel 2000
# DJIA
# NASDAQ 100?
# There is overlap in those lists so ensure no duplicates
# Then get updates since the last time

# Feature engineering:
# Create a 'WentUp' column which determines if closing price is greater than previous day

#Goal of this project is to predict if a stock or index is going to go up 
#tomorrow.  
#
#Approach
#Initially just train n models, one for each stock, to predict if 
#that stock is expected to go up the next day.  
#Eventually would expect to get to ensemble models using highest likelihood 
#stocks, etc.
#
#Structure
#There will be a module to manage the list of stocks and other features
#This will need initial creation and then to apply updates.  If applying 
#updates, then need to understand what changed (i.e. stock added) and then
#go get the data
#
#There will be a module to update data.  This could be separated into 
#initial data gathering and getting updated/new data.  Since getting
#updated/new data will involve getting a subset of all available data and then
#comparing dates or other parameters, it might be expensive to use this 
#approach for initial data gathering.

#There will be a module that lists all parameters (stocks, indices, etc.) and
#how to update them.  There will be submodules to build thequery and update 
#each.

#Would be really neat to keep a transaction log and the historical data
#for the parameters and data.  Thus could look back in time and see what 
#we had for parms, data, models, etc.
 
#
#There will be a module to take the data gathered and generate a view that
#is acceptable / useful for machine learning tools or algorithms.
#
#There will also need to have a feature engineering piece to build the various
#output columns.  
#
#Envisioning building multiple classification models, one for each stock
#or index.



APIkey='850FIAHPBVATO1OQ'

import requests
import json
import datetime
url='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&outputsize=full&apikey=850FIAHPBVATO1OQ&datatype=csv'
#res = requests.get(url)
#print(res.status_code)
#print(res.text)

russell_2000 = open('russell_2000.txt', 'r')
stocks_2000 = russell_2000.readlines()
stock_list = []
for stock in stocks_2000:
    ticker = stock.splitlines()
    stock_list.append(ticker[0])
print(stock_list)



