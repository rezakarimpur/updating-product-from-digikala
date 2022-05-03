# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:26:40 2021

@author: Nima
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:57:47 2020

@author: Nima
"""


import requests
import logging
from datetime import datetime
from typing import Iterator
from pytz import utc
import re
import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import timeit
import os
import datetime
import pandas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

from selenium import webdriver



driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")


start = timeit.default_timer()
pdLinksAll=[]
#urlstring="https://www.digikala.com/search/category-laptop/?brand[0]=6&"
pdLinks=[]
for pageNo in range(0,1):
    
    #insert digikala url in this part with format  like below
    #split url in to 2part dividing by page number
    #url="https://www.digikala.com/brand/pars-khazar/?category[0]=5815&pageno="+str(pageNo)+"&last_filter=category&last_value=5815&sortby=4"
    #you should check if the category page has 1 or more pages then use one of the url below
    #url="https://www.digikala.com/search/category-ups-battery/?pageno="+str(pageNo)+"&sortby=4"
    url="https://www.digikala.com/search/category-washing-machines/?brands[0]=1106"
    print(url)
    driver.get(url)

    #response = requests.get(url)
    #content = response.content.decode('utf-8')
    #soup = BeautifulSoup(response.content, 'html.parser')
    content=driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    a=soup.find_all('div', attrs={'class':'border-b'})
    for item in a:
        for aElement in item.find_all('a', href=True):
         link_text = aElement['href']
         
         product={'url':str("https://www.digikala.com"+link_text)}    
         print(link_text)
         pdLinks.append(product)
driver.close()    
with open('data.txt', 'w') as outfile:
    json.dump(pdLinks, outfile)
     



