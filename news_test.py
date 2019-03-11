#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 08:46:38 2019

@author: colemanda
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:21:52 2019

@author: david_000
"""

import requests
import json
import datetime

from myhtmlparser import MyHTMLParser




html_chaff = ['<!DOCTYPE html>', 
              '<html>\n','<head>',
              '<title>Weather Information</title>',
              '</head>',
              '<body>',
              '<h1>Leave me Alone!</h1>',
              '<p>I hate all of you</p>']

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


url = 'https://www.seattletimes.com'

html_filename = 'news.html'

raw_file = open('rawdata2.txt', 'w')
# open the file and write most HTML stuff in it

res = requests.get(url)
#    print(res.status_code)
#    print(res.text)
raw_file.write(res.text)
raw_file.write('\n')

raw_file.close()

url_list = ['https://www.seattletimes.com/seattle-news/politics/how-amazon-gets-whatever-it-wants/',
            'https://www.seattletimes.com/seattle-news/homeless/homeless-man-dies-from-exposure-service-providers-prepare-for-more-cold-weather/',
            'https://www.seattletimes.com/seattle-news/transportation/more-snow-is-headed-toward-seattle-and-road-clearing-crews-are-getting-ready/',
            'https://www.seattletimes.com/seattle-news/politics/should-seattle-make-trims-to-neighborhood-upzones-plan-city-council-wades-into-debate/',
            'https://www.seattletimes.com/business/tensions-over-political-resistance-to-amazon-boil-over-in-new-york/',
            'https://www.seattletimes.com/seattle-news/health/washington-lawmakers-weigh-stricter-vaccine-bill-amid-outbreak/']
    

count = 0
for url2 in url_list:
    res = requests.get(url2)
    raw_file = open('file' + str(count) + '.txt', 'w')
    raw_file.write(url2)
    raw_file.write('\n')
    raw_file.write(str(res.status_code))
    raw_file.write('\n')
    raw_file.write(res.text)
    raw_file.write('\n')
    raw_file.close()
    count = count + 1


res = requests.get(url_list[0])
parser = MyHTMLParser()
parser.feed(res.text)

raw_file = open('sampledata.txt', 'w')
for stuff in parser.p_data:
    raw_file.write(stuff)

raw_file.close()


    