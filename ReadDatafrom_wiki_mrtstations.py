# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:23:25 2020

@author: theiv
"""
#trying to read in Wikipedia Data 

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


URL = "https://en.wikipedia.org/wiki/List_of_Singapore_MRT_stations"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')

My_table = soup.find('table',{'class':'wikitable'})
My_table 

links = My_table.findAll('a')
links

Station = []
for title in links:
    Station.append(title.get('title'))
#print(Station)


mrts = pd.DataFrame()
List_of_Stations = pd.DataFrame()
pattern = r'(?=.*MRT)(?=.*station)'

mrts['Station'] = Station
mrts['MRT_Y']  =  mrts['Station'].str.contains(pattern)





