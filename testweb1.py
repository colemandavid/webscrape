# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:21:52 2019

@author: david_000
"""

import requests
import json

res = requests.get('https://api.weather.gov/points/47.6966153,-122.6709335')
type(res)
print(res.status_code)
print(res.text)

parsed_json = json.loads(res.text)
forecast_url = parsed_json['properties']['forecast']
print('Forecast url: ' + forecast_url)


res2 = requests.get(forecast_url)
type(res2)
print(res2.status_code)
print(res2.text)

forecast_json = json.loads(res2.text)
first_temp = forecast_json['properties']['periods'][0]['startTime']
print('start time: ' + first_temp)

for i in range(len(forecast_json['properties]['periods'])):
    

