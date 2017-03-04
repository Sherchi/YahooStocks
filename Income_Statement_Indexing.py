def IS(symbol):
    import time # used to measure the length of time the program takes to run
    #start_time = time.time()
    from lxml import html # html parser. needed for bs?
    import requests # needed to request the url.
    from bs4 import BeautifulSoup # parser for html better than lxml
    from unicodedata import normalize # function needed to remove &b8 or something
    import locale # no idea
    import re # dont know

    ##---------Block 1 ----------
    locale.setlocale(locale.LC_ALL, "english_USA")
    url = 'http://ca.finance.yahoo.com/q/is?s=' + symbol
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, "lxml")

    ##-----------Block 2 ------------
    try:
        data2 = soup.find("table", class_="yfnc_tabledata1").find("tr").find("td").find("table", width="100%").find_all("tr")
        test = 0
    except:
        test = 1
#------------block 3-------------
    if test != 1:
        #--------------block 3.1 --------------
        data2 = soup.find("table", class_="yfnc_tabledata1").find("tr").find("td").find("table", width="100%").find_all("tr")
        Flist = []
        for i in range(len(data2)):
            data3 = data2[i].find_all(["td", "th"])
            value = []
            for j in range(len(data3)):
                value.append(data3[j].text)
            Flist.append(value)
#       #---------------block 3.2----------------------
        for i in range(len(Flist)):
            for j in range(len(Flist[i])):
                #Replaces all the /xa0 andother unicodes with
                string = Flist[i][j]
                string = normalize("NFKD", string)
                string = string.replace(",","").replace("-","0").replace("(","-").replace(")","").strip()
                try: #tries out to see if the data scraped is a string or a float
                    string = float(string)
                    check = 0
            #       might include a matrix here to record which are values are
            #       floats and which ones are strings
                except:
                    check = 1
                       
                if check == 1:
                    Flist[i][j] = string
                else:
                    Flist[i][j] = float(string)

        return Flist

    else:
        return "N/A"


#for i in range(len(Flist)):
 #   print("Index: ", i, " -- ", Flist[i])

#print("%s seconds" % (time.time()-start_time))
