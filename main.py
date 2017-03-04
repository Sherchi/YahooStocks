import time # imports time. Allows for recording of runtime.
from Income_Statement_Indexing import IS # allows for scraping of Income statement from yahoo
from Balance_Sheet_Indexing import BS # Allows for scraping of balance sheet from yahoow
start_time = time.time() #initializes time at this point as zero
import csv

# ------Block 1----------
with open('NASDAQ.csv', 'r') as f:
    reader = csv.reader(f)
    SList = list(reader)
test = 0

for i in range(len(SList)):
    del SList[i][1]
    del SList[i][1]
    del SList[i][1]
    del SList[i][1]
    del SList[i][3]

print("Running. DO NOT TOUCH PLEASE")
# ----------Block 2----------

for i in range(len(SList)):
    IncomeS = IS(SList[i][0])
    BalanceS = BS(SList[i][0])
    try :
        ROE = IncomeS[34][1]/BalanceS[46][1]
        ROA = IncomeS[34][1]/BalanceS[19][1]
        BES = (IncomeS[4][1]-IncomeS[15][1])*IncomeS[1][1]/IncomeS[4][1]
        SList[i].extend([IncomeS[0][1],ROE,ROA,BES])
    except:
        test = 1
    if test != 1:
        test = 0
    else:
        SList[i].append("N/A")
        test = 0

#print(SList)
# ------------------Block 3--------------

f = open('ListF.txt', 'w')
writingf = csv.writer(f, delimiter=',', quotechar = '"')
g = open('ListM.txt', 'w')
writingg = csv.writer(g, delimiter=',', quotechar = '"')
for i in range(len(SList)):
    try:
        SList[i][5] = float(SList[i][5])
        SList[i][6] = float(SList[i][6])
        test = 0
    except:
        test = 1
    if test != 1:
        if SList[i][5]<0 or SList[i][6]<0: 
                writingf.writerow(SList[i])
                #print(["Test ----   ", SList[i]])
        else:
                writingg.writerow(SList[i])
    else:
        test = 0

f.close()
g.close()



print("%s seconds" % (time.time()-start_time))
