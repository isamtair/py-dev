import csv
import sys

def doFile():

    with open(sys.argv[1], "r") as f:
        csvReader=csv.reader(f, delimiter=";")
        next(f)
        for row in csvReader:
            TS, ID, Date, Loc, Zip, Pri= row
            print row
        #print (f.read())


doFile()