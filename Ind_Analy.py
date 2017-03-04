import csv
from numpy import unique
from operator import itemgetter
with open('NASDAQ.csv', 'r') as f:
    reader = csv.reader(f)
    list1 = list(reader)

listB = list([''] for i in range(len(list1)))
for i in range(len(list1)):
    listB[i] = list1[i][6]
    
list2 = unique(listB)
list3 = list(['',''] for i in range(len(list2)))

listtest = list2[1]

for i in range(len(list2)):
    listtest = list2[i]
    list3[i][0] = listtest   
    list3[i][1] = listB.count(list3[i][0])
    

with open('ListM.txt', 'r') as f:
    reader = csv.reader(f)
    list1 = list(reader)

listB = list([''] for i in range(len(list1)))
for i in range(len(list1)):
    try:
        listB[i] = list1[i][2]
    except:
        listB[i] = ''

for j in range(len(list2)):
    list3[j].append(listB.count(list3[j][0]))
    list3[j].append(list3[j][2]/list3[j][1])

list3.sort(key = itemgetter(1), reverse = True)
list3.sort(key = itemgetter(3), reverse = True)
#sorted(list3, key = lambda i: i[3], reverse = True)

g = open('ListInd.csv','w')
writingf = csv.writer(g, delimiter = ',')

for i in range(len(list3)):
    if float(list3[i][3]) >0.1:
        writingf.writerow(list3[i])
g.close()
print(list3[5])

g = open('ListInd.csv', 'r')
list4 = list(csv.reader(g))
list4 = list(filter(None, list4))
print(list4)
