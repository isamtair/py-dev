#First python
import sys
from os import path

print ("Hi")
print "Lets see what names you have in mind"



def read_names():
    names = []
    leave = 'exit'
    while True:
        name = raw_input("Enter your name: ")
        if name==leave:
            print names
            print "Leaving now, GoodBye !!!"
            exit()
        else:
            name.upper()
            names.sort()
            names.append(name)
            print names
            names.reverse()
            #sorted_names=names.sorted(names)
            print names
            #print sorted_names

        #print "length of name is:", len(name), "length of list is: ", len(names), names
read_names()