import requests
from bs4 import BeautifulSoup
import time
import asyncio
import json


def propertyDetail(url):
    
    print("running...")
    
    result = requests.get(url)
    
    
    src = result.content
    
    # soup = BeautifulSoup(src, 'lxml')
    
    
    inJson = json.loads(src)
    
    # title = soup.find(class_="style_price__Wd9v5")
    
 
    return inJson['pageProps']['serverPropertyDetails']['property']

    