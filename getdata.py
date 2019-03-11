#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:05:13 2019

@author: colemanda
"""

import requests
import json
import datetime
url='https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MSFT&apikey=850FIAHPBVATO1OQ&datatype=csv'
res = requests.get(url)
print(res.status_code)
print(res.text)
