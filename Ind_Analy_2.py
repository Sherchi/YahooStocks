import csv
from numpy import unique
from Income_Statement_Indexing import IS
from Balance_Sheet_Indexing import BS
from operator import itemgetter
with open('ListInd.csv', 'r') as f:
    reader = csv.reader(f)
    list1 = list(reader)

list1 = list(filter(None, list1))

for i in range(len(list1)):
    del list1[i][1]
    del list1[i][1]
    del list1[i][1]

listfin = list([''] for i in range(len(list1)))
for i in range(len(listfin)):
    listfin[i].append(list1[i][0])
    del listfin[i][0]
    
with open('NASDAQ.csv', 'r') as f:
    reader = csv.reader(f)
    list2 = list(reader)
list2 = list(filter(None,list2))

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i][0] == list2[j][6]:
            list1[i].append(list2[j][0])


for i in range(len(list1)):
    revtot = 0
    count = 0
    ROAavg = 0
    ROAtop = -50
    ROAbot = 50
    ROA = 0
    for j in range(len(list1[i])-1):
        
        IncomeS = IS(list1[i][j+1])
        BalanceS = BS(list1[i][j+1])
        try:
            revtot = IncomeS[1][1]+revtot
            count = count+1
            ROA1 = IncomeS[37][1]/BalanceS[48][1]
            if ROA1 > ROAtop:
                ROAtop = ROA1
            if ROA1 < ROAbot:
                ROAbot = ROA1
            ROA = ROA+ROA1
        except:
            None
    ROAavg = ROA / count
    listfin[i].append(revtot)
    listfin[i].append(ROAavg)
    listfin[i].append(ROAtop)
    listfin[i].append(ROAbot)
    listfin[i].append(count)

with open('Ind_Sum.csv', mode = 'w') as f:
    writingf = csv.writer(f, delimiter = ',')
    for i in range(len(listfin)):
        writingf.writerow(listfin[i])
    f.close()
        
