import sys
import csv


with open(sys.argv[1], "r") as f:
    reader=csv.reader(f, delimiter=';')

    for row in reader:
        TS, ID, Date, Zip, Loc, Pri= row
        print TS
    #print (f.read())
