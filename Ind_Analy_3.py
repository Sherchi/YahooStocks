import csv
from numpy import unique
from Income_Statement_Indexing import IS
from Balance_Sheet_Indexing import BS
from operator import itemgetter
from tabulate import tabulate

with open('Ind_Sum.csv', 'r') as f:
    reader = csv.reader(f)
    list1 = list(reader)

list1 = list(filter(None, list1))

list2 = list([''] for i in range(len(list1)))

koko = "start"

while koko != "end":

    for i in range(len(list2)):
        list2[i][0] = list1[i][0]
        print('Index - ', i, ' -- ', list2[i][0])

    for i in range(1):
        try:
            IndIndex = int(input('Please enter index number:  '))
            print('Entered index number: ', IndIndex, ' industry: ', list2[IndIndex][0])
        except:
            i = i-1

    with open('NASDAQ.csv', 'r') as f:
        reader = csv.reader(f)
        listM = list(reader)

    symb = []

    for i in range(len(listM)):
        if listM[i][6] == list2[IndIndex][0]:
            symb.append(listM[i][0])

    list3 = list([''] for i in range(len(symb)))

    for i in range(len(symb)):
        IncomeS = IS(symb[i])
        BalanceS = BS(symb[i])
        try:
            list3[i][0] = symb[i]
            ## Resources Analysis Start
            date = BalanceS[0][1]
            list3[i].append(date) ## [*][1]
            CurrAss = BalanceS[4][2]+BalanceS[5][2]+BalanceS[6][2]+BalanceS[7][2]+BalanceS[8][2]
            list3[i].append(CurrAss) ## [*][2]
            PPE = BalanceS[12][1]
            list3[i].append(PPE) ## [*][3]
            PerPPE = BalanceS[12][1]/BalanceS[19][1]
            list3[i].append(round(PerPPE,4)) ## [*][4]
            LTI = BalanceS[11][1]
            list3[i].append(LTI) ## [*][5]
            PerLTI = BalanceS[11][1]/BalanceS[19][1]
            list3[i].append(round(PerLTI,4)) ## [*][6]
            list3[i].append("--") 
            ## Operations Analysis Start
            try:
                ROA = IncomeS[34][1]/BalanceS[48][1]
                list3[i].append(round(ROA,4)) ## [*][8]
            except:
                list3[i].append("N/A")   
            Rev = IncomeS[1][1]
            list3[i].append(Rev) ## [*][9]
            PerRet = IncomeS[34][1]/IncomeS[1][1]
            list3[i].append(round(PerRet,4)) ## [*][10]
            TotCost = IncomeS[1][1]-IncomeS[34][1]
            list3[i].append(round(TotCost,4)) ## [*][11]
            PerRevCost = IncomeS[2][1]/TotCost
            list3[i].append(round(PerRevCost,4)) ## [*][12]
            PerSelling = IncomeS[8][2]/TotCost
            list3[i].append(round(PerSelling,4)) ## [*][13]
            PerRD = IncomeS[7][2]/TotCost
            list3[i].append(round(PerRD,4)) ## [*][14]
            PerOther = (IncomeS[9][2]+IncomeS[10][2]+IncomeS[18][2]+IncomeS[20][2]+IncomeS[22][2]+IncomeS[23][2])/TotCost
            list3[i].append(round(PerOther,4)) ## [*][15]
        except:
            for j in range(13):
                list3[i].append('N/A')

    print(tabulate(list3, headers = ['symbol', 'date', 'Curr Ass', 'PPE', '%PPE', 'LTI', '%LTI', '--', 'ROA', 'Rev', '%Ret', 'Tot Costs', '%CostRev', '%Sell', '%R&D', '%Others']))

    koko = input('type end to end program:   ')
