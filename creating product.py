# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 16:11:59 2020

@author: Nima
"""

# -*- coding: utf-8 -*-
"""
************************!!!!!!attention!!!!!!!!*************************  
#******you shold create new category in woocomerce and
#******then replace it in cat  in start of getting product variation  part
#************************DO not Change any thingelse
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
from woocommerce import API
                
wcapi = API(
url="https://tasisplus.ir",
consumer_key="put your woocomerce api key",
consumer_secret="put your woocomerce secret key",
version="wc/v3",
timeout=90
)
        
f= open('data.txt')
pdUrl=json.load(f)   

start = timeit.default_timer()

from selenium import webdriver

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")


    
iii=0 
for urll in pdUrl:
   
    url=urll['url']

    url="https://www.digikala.com/product/dkp-7012507/%D8%AF%D8%B3%D8%AA%DA%AF%D8%A7%D9%87-%D8%AA%D8%B5%D9%81%DB%8C%D9%87-%DA%A9%D9%86%D9%86%D8%AF%D9%87-%D9%87%D9%88%D8%A7-%D8%B3%D8%A7%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-blue-sky/"
    
    #=============================start of reciving product atts
    driver.get(url)
    content=driver.page_source
    print("1- ","done response")
    #*************************************
    
   
    soup = BeautifulSoup(content, 'html.parser')
     
    aa=[]
    bb=[]
    
    
    for item in soup.find_all('div', attrs={'class':'w-full d-flex last PdpSpecification_PdpSpecification__valuesBox__smZXG'}):
        
       a= item.find('p')
       if a is not None:
    
        a= item.find('p').text   
        aa.append(a)
       else:
        a=""     
        aa.append(a)
       print(a)
    
    for item in soup.find_all('div', attrs={'class':'border-b py-2 py-3-lg grow-1'}):
       b= item.find('p').text.strip()
       bb.append(b)
       print(b)
    att=[]
    pdAttribiutName=[]  
    if (len(aa)== len(bb)):
        for i in range (len(aa)):
            
            ats= {"name":aa[i],"position":0,"visible":True,"variation":False,"options":bb[i]}
            att.append(ats)
                
    
            att.append(ats)
    #====================start of geting product short description
    
    if soup.find('p', attrs={'class':'text-body-1 color-800'}) is not None:
         
          shortDescriptionForEveryProduct= soup.find('p', attrs={'class':'text-body-1 color-800'}).text.strip()
    else:
          shortDescriptionForEveryProduct=""
  
    #************************ start of getting product name 
    print("3- ","done short description and atts")
    
    titleFa=soup.find('h1', attrs={'class':'text-h4 color-900 mb-2'}).text.strip()
    #titleEn=soup.find('span', attrs={'class':'c-product__title-en'}).text.strip()
    pdTitle=[]
    pdTitle.append({"title1":titleFa})
    #pdTitle.append({"title2":titleEn})
    #****************************start of getting product images********************
    print("4- ","done title")
    
    images=[]
   
    for item in soup.find_all('div', attrs={'class':'d-flex flex-column ai-center max-w-92-lg max-w-145-xl d-none d-block-lg mb-2'}):
      img=item.find_all('img') 

    for x in img: 
        
         ats= {"src":str(x['src']), "name": str(titleFa),"alt":str(titleFa)}
         images.append(ats)

    

    print("4- ","done images")

#********************************************creating product
    
    cat1="1760"
    cat2="1764"
    cat3="9630"   
    #cat4="9554"   

    simpleProductData = {
        "name": str(titleFa),
        "type": "simple",
        "regular_price": str(""),
        "description":shortDescriptionForEveryProduct,
        "short_description": shortDescriptionForEveryProduct,
        "categories": [
            {
                "id":cat1
            },
            {
                "id": cat2
            },     {
                "id": cat3
            },
                #{"id": cat4   }
        ],
        "images":images,
        "alt": {
          "description": str(titleFa),

        },
        "attributes":att,
        "status":"private",     
                   
    }
    print(wcapi.post("products", simpleProductData).json())

    print("the link number is "+str(iii))
    iii=iii+1
    
    
    
    
    

    
    
    
    
    




      
      
   
