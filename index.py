
# YouTube Link:

# Ensure that you have both beautifulsoup and requests installed:
#   pip install beautifulsoup4
#   pip install requests

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from PropertyDetail import propertyDetail



def substring_after(s, delim):
    return s.partition(delim)[2]


for x in range(114,124):
      
  result = requests.get("https://www.graana.com/house/for_sale/islamabad/all/1?offset=" + str((x - 1) * 30) + "&page=" + str(x) )
   
  print(result.status_code)

  src = result.content

  soup = BeautifulSoup(src, 'lxml')

  links = soup.find_all(class_="style_product_image__UOxoC")

  urlList = []

  for link in links: 
    tempString = link.attrs['href']
    substring_after(tempString, "www.graana.com/property/")
    try:
      data = propertyDetail("https://www.graana.com/_next/data/_AQ71uyDCBQO69pU7xTYw" + tempString + ".json")
      urlList.append({
        "link":"https://www.graana.com/_next/data/_AQ71uyDCBQO69pU7xTYw" + tempString + ".json",
         **data
         })
    except:
      print("exception occured", "https://www.graana.com/_next/data/_AQ71uyDCBQO69pU7xTYw" + tempString + ".json")
     
     
  #  print(urlList[1]["link"])
  #  propertyDetail(urlList[1]["link"])
 
  MongoUri = "mongodb://localhost:27017"

  client = MongoClient(MongoUri)

  db = client.pythonScraping
   
  houseForRent = db.IslamabadHousesForSale
   
  result = houseForRent.insert_many(urlList)
  
  print("MongoDB response:", result)
  
  print("Document inserted no.:", x)
  
  print("******************************&&&&&&&&&&&&&&&&&&&&&&&&******************************")