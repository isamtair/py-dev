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
            print "Leaving now, GoodBye !!!"
            exit()
        else:
            names.append(name)
            print names[0], len(name), len(names)
read_names()

