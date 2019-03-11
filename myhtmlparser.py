#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 09:45:12 2019

@author: colemanda
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.p_count = 0
        self.p_data = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.p_count = self.p_count + 1
#            print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        if tag == 'p':
            self.p_count = self.p_count - 1
#            print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.p_count > 0:
            self.p_data.append(data)
#            print("Encountered some data  :", data)


