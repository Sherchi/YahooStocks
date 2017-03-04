import time
start_time = time.time()
from lxml import html
import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import locale
import re
locale.setlocale(locale.LC_ALL, "english_USA")
page = requests.get('http://ca.finance.yahoo.com/q/is?s=MSFT')
data = page.text
soup = BeautifulSoup(data, "lxml")
data2 = soup.find("table", class_="yfnc_tabledata1").find("tr").find("td").find("table", width="100%").find_all("tr")

#start loop here. Have data 3, be a table of all data 2 lists. 
data3 = data2[2].find_all("td")

value = data3[0].text
value = normalize("NFKD", value) #Replaces all the /xa0 and other unicodes with
                                #their respective characters
try: #tries out to see if the data scraped is a string or a float
    value2 = float(value.replace(",",""))
    check = 0
    # might include a matrix here to record which are values are
    #floats and which ones are strings
except ValueError:
    print("Not a float")
    check = 1
                   
# Prints out the data. 
if check == 1:
    value2 = value
else:
    value2 = float(value.replace(",",""))

print(value2)

print("%s seconds" % (time.time()-start_time))
