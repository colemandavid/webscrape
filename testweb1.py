# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:21:52 2019

@author: david_000
"""

import requests
import json
import datetime


raw_data = False
small_images = False


weekday_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dt_list = []
city_list = []

# List of cities, each entry for a city is a dictionary
# of dt, temp
data_stuff = {}

html_chaff = ['<!DOCTYPE html>', 
              '<html>\n','<head>',
              '<title>Weather Information</title>',
              '</head>',
              '<body>',
              '<h1>Weather Consolidator</h1>',
              '<p></p>']

html_table_start = '<table border="1" style="width:100%">'
html_table_header_start_tag = '<th>'
html_table_header_end_tag = '</th>'

html_nested_table_start = '<table>'

html_table_row_start_tag = '<tr>'
html_table_row_end_tag = '</tr>'

html_table_cell_start_tag = '<td align="center" valign="top">'
html_table_cell_end_tag = '</td>'

html_table_end = '</table>'

html_end = ['</body>',
            '</html>']

coordinates = [['Silverdale',47.6966153,-122.6709335],
               ['Vancouver',45.6194858,-122.5583884],
               ['Camas',45.5884891,-122.3964411],
               ['Snoqualmie Pass', 47.4175404,-121.4171913],
               ['Newport',41.4801521,-71.3037436],
               ['Norfolk',36.8132967,-76.2892189],
               ['Washington, DC',38.89378,-77.1546627],
               ['Manassas',38.7447207,-77.5221135],
               ['Winston-Salem',36.1047679,-80.383545],
               ['Boise',43.6028311,-116.203961],
               ['Pateros',48.0559732,-119.9155396]]

api_url = 'https://api.weather.gov/points/'

html_filename = 'weather.html'

if raw_data:
    raw_file = open('rawdata.txt', 'w')
    
# open the file and write most HTML stuff in it

for places in coordinates:

    url = api_url + str(places[1]) + ',' + str(places[2])
    print(url)
    if raw_data:
        raw_file.write(url)
        raw_file.write('\n')
    
    res = requests.get(url)
#    print(res.status_code)
#    print(res.text)
    if (raw_data):
        raw_file.write(res.text)
        raw_file.write('\n')
    
    parsed_json = json.loads(res.text)
    forecast_url = parsed_json['properties']['forecast']
    print('forecast_url: ' + forecast_url)

    if (raw_data):
        raw_file.write('forecast_url: ' + forecast_url)
        raw_file.write('\n')
    
    city = parsed_json['properties']['relativeLocation']['properties']['city']
    print(city)
    
    
    res2 = requests.get(forecast_url)
    print(res2.status_code)
    if res2.status_code != 200:
        continue
#    print(res2.text)
    if (raw_data):
        raw_file.write(res2.text)
        raw_file.write('\n')
    
    pj2 = json.loads(res2.text)
    
    data_stuff[places[0]] = {}
    
    for i in range(len(pj2['properties']['periods'])):
        start_time = pj2['properties']['periods'][i]['startTime']
        sdate, stime = start_time.split('T')
#        print( start_time, sdate, stime)
        year, month, day = sdate.split('-')
        stime, tz = stime.split('-')
        hour, minute, second = stime.split(':')
        
        ihour = int(hour)
        if (ihour >=0 and ihour<6):
            ihour = 18
        if (ihour >= 6 and ihour <18):
            ihour = 6
        if (ihour >= 18 and ihour <=23):
            ihour = 18
            
#        print(year, month, day, hour, minute, second)
        start_dt = datetime.datetime(int(year), int(month), int(day), 
                                     ihour, int(minute), int(second))
        if start_dt not in dt_list:
            dt_list.append(start_dt)
#        print(start_dt)
        temp = pj2['properties']['periods'][i]['temperature']
        short = pj2['properties']['periods'][i]['shortForecast']
        image = pj2['properties']['periods'][i]['icon']
        if small_images:
            image = image.replace('medium', 'small')
        data_stuff[places[0]][start_dt] = [temp, short, image]
# close out the table

dt_list.sort()
print(dt_list)

weather_file = open(html_filename, 'w')
for chaff in html_chaff:
    weather_file.write(chaff)
    weather_file.write('\n')

weather_file.write(html_table_start)
weather_file.write('\n')
weather_file.write(html_table_row_start_tag)
weather_file.write('\n')
weather_file.write(html_table_header_start_tag)
weather_file.write('City')
weather_file.write(html_table_header_end_tag)
weather_file.write('\n')

for dt in dt_list:
    weather_file.write(html_table_header_start_tag)
#    weather_file.write(dt.strftime('%a') + '</br>' + dt.strftime('%d %b') + 
#                       '</br>' + dt.strftime('%H%M'))
    if ((dt.hour >= 0) and (dt.hour < 6)):
        strdate ='Night'
    elif ((dt.hour >= 6) and (dt.hour < 18)):
        strdate = 'Day'
    elif ((dt.hour >= 18) and (dt.hour <= 23)):
        strdate = 'Night'
        
    weather_file.write(dt.strftime('%a') + '</br>' + strdate + '</br>' + 
                       dt.strftime('%d %b') )
    weather_file.write(html_table_header_end_tag)
    weather_file.write('\n')

weather_file.write(html_table_row_end_tag)
weather_file.write('\n')

for places in coordinates:
    weather_file.write(html_table_row_start_tag)
    weather_file.write('\n')
    weather_file.write(html_table_cell_start_tag)
    weather_file.write(places[0])
    weather_file.write(html_table_cell_end_tag)
    weather_file.write('\n')

    for dt in dt_list:
        weather_file.write(html_table_cell_start_tag)
        if places[0] in data_stuff:
            entry = data_stuff[places[0]].get(dt,'   ')
        else:
            entry = '   '

        # Inner nested table, in each cell            
        weather_file.write(html_nested_table_start)
        weather_file.write('\n')

        # First row/cell in inner table, temp
        weather_file.write(html_table_row_start_tag)
        weather_file.write('\n')
        weather_file.write(html_table_cell_start_tag)
        
        weather_file.write(str(entry[0]))
        
        weather_file.write(html_table_cell_end_tag)
        weather_file.write('\n')
        weather_file.write(html_table_row_end_tag)
        weather_file.write('\n')

        # Another row/cell, image
        weather_file.write(html_table_row_start_tag)
        weather_file.write('\n')
        weather_file.write(html_table_cell_start_tag)
        
        weather_file.write('<img src=' + entry[2] + '>')
        
        weather_file.write(html_table_cell_end_tag)
        weather_file.write('\n')
        weather_file.write(html_table_row_end_tag)
        weather_file.write('\n')
        
        # Second row/cell in inner table, short forecast
        weather_file.write(html_table_row_start_tag)
        weather_file.write('\n')
        weather_file.write(html_table_cell_start_tag)
        
        weather_file.write(str(entry[1]))
        
        weather_file.write(html_table_cell_end_tag)
        weather_file.write('\n')
        weather_file.write(html_table_row_end_tag)
        weather_file.write('\n')

        weather_file.write(html_table_end)
        weather_file.write('\n')
        
        # Inner nested table now closed out


        # Close out this cell (for a given City, timestamp pair)
        weather_file.write(html_table_cell_end_tag)
        weather_file.write('\n')


    # Close out the row for the City
    weather_file.write(html_table_row_end_tag)
    weather_file.write('\n')

# Close out the outer/entire table
weather_file.write(html_table_end)
weather_file.write('\n')

for end_stuff in html_end:
    weather_file.write(end_stuff)
    weather_file.write('\n')
    
weather_file.close()
if (raw_data):
    raw_file.close()

# print(data_stuff)
    
#res = requests.get('https://api.weather.gov/points/47.6966153,-122.6709335')
#type(res)
#print(res.status_code)
#print(res.text)

#parsed_json = json.loads(res.text)
#forecast_url = parsed_json['properties']['forecast']
#print('Forecast url: ' + forecast_url)


#res2 = requests.get(forecast_url)
#type(res2)
#print(res2.status_code)
#print(res2.text)
#
#forecast_json = json.loads(res2.text)
#first_temp = forecast_json['properties']['periods'][0]['startTime']
#print('start time: ' + first_temp)
#
#for i in range(len(forecast_json['properties']['periods'])):
#    name = forecast_json['properties']['periods'][i]['name']
#    temp = forecast_json['properties']['periods'][i]['temperature']
#    short = forecast_json['properties']['periods'][i]['shortForecast']
#    
#    print(name + ' temp: ' + str(temp) + ' ' + short)
    

