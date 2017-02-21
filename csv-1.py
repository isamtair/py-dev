import csv
import sys

from os import path

"""""""""
def readFile():
    row_number=0
    with open('c:\users\isam\desktop\ml_cdr_data_2016_02_24_05_00.csv', "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            if i < 10:
                print 'line[{}] = {}'.format(i, line)
readFile()


def readFile():
    row=0
    with open('c:\users\isam\desktop\ml_cdr_data_2016_02_24_05_00.csv','r') as inputF:
        newFile=csv.reader(inputF)
        newList= list(newFile)
        for row  in newList:
            while row <0:
                print newList[row]

readFile()


def readlines():
   counter=0
   row_number=0
   inputF=csv.reader(open('c:\users\isam\desktop\ml_cdr_data_2016_02_24_05_00.csv', "r"), delimiter=';', quotechar='|')
   listF= list(inputF)
   while counter <5:
       counter+=1
       print " ",counter, " ", listF[counter], len(listF[counter])
   while row_number <=5:
       for row in listF :
           print row[0], row[1]
   counter+=1

readlines()
"""""

def useDic():
    count=0
    infile= csv.reader(open('c:\users\isam\desktop\ml_cdr_data_2016_02_24_05_00.csv', "r"), delimiter=';', quotechar='|')
    inDic={}
    while count<5:
        for line in infile:
            if line[5] != "1":
                print line[0],line[1], line[2], line[3], line[4], line[5]
useDic()

