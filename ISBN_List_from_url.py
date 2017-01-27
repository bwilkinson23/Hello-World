import csv
import urllib.request
from bs4 import BeautifulSoup
import ftplib

### OPEN LOCAL FILE
#f = open('example_solr_export.csv', 'r', encoding='utf-8')
#csv_f = csv.reader(f)

url = 'http://sandbox.lbcc.linnlibraries.org/example_solr_export.csv'
#response = urllib.request.urlopen(url)
#cr = csv.reader(response)
response = urllib.request.urlopen(url)
text =  response.read().decode('utf-8')

soup = BeautifulSoup(text, 'html.parser')
cr = csv.reader(soup.pre.get_text().split("\n"), delimiter=',', quotechar='"')

ISBN_postsort = []

for row in cr:
    if len(row) >1:
        #print (row[5])
        if row[5] != "":
            ISBN_postsort.append(row[5])

#print (ISBN_postsort)

isbnList = []

### ISBN Header
isbnHeader = ISBN_postsort[0]
data = ISBN_postsort
### singleISBN is a list ['isbn','isbn2' ....] 

singleISBN = []

for i in range(len(data)):
    testISBN = data[i].split(',')
    if len(testISBN) >1:
        for i in range(len(testISBN)):
            singleISBN.append(testISBN[i])

#print (singleISBN)

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

with open('ISBN_List.csv','w') as fp:
    a = csv.writer(fp,delimiter=',', lineterminator='\n')
    data = testISBN
    a.writerows(data)

#print(data)


