import csv


### OPEN LOCAL FILE
f = open('CSV_FILE_NAME.csv', 'r', encoding='utf-8')
csv_f = csv.reader(f)

#print (f)  ##_io.Text location
isbnList = []


print(csv_f)
print(f)
### Eliminate HTML and make list of ISBN numbers
### List elements are concatenated.
for row in csv_f:
    #print (row)
    if len(row) >= 4 and row[5] != "":
       isbnList.append(row[5])


### ISBN Header
isbnHeader = isbnList[0]

### Test print
data = isbnList
#print (data)


### singleISBN is a list ['isbn','isbn2' ....] 

singleISBN = []

for i in range(len(data)):
    testISBN = data[i].split(',')
    if len(testISBN) >1:
        for i in range(len(testISBN)):
            singleISBN.append(testISBN[i])

print (singleISBN)

### testISBN is a sequence [['isbn1'], ['isbn2'] ... ]
            
testISBN = []

for i in range(len(singleISBN)):
    mListISBN = [singleISBN[i]]
    testISBN.append(mListISBN)

#print (testISBN)

### This is to see theISBN printed one after another
for i in range(len(data)):
    splitISBN = data[i].split(",")

#print (splitISBN)

with open('NAME_NEW_CSV_FILE.csv','w') as fp:
    a = csv.writer(fp,delimiter=',', lineterminator='\n')
    data = testISBN
    a.writerows(data)

#print(data)


