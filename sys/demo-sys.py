#!/usr/local/bin/python

import sys

print("sys.argv:")
print(repr(sys.argv))
print

print("This script relative to the execution folder: "+ sys.argv[0])
print

print("sys.path:")
print(repr(sys.path))
print

print("The absolute path of where this script is: "+sys.path[0])
print

print("Dictionary of loaded modules: "+repr(sys.modules))

def myExcepthook(type, value, traceback):
    print 
    print type
    print value
    print traceback


def sayGoodbye():
    print
    print sys.last_type #  type of last uncaught exception
    print sys.last_value # value of last uncaught exception
    print sys.last_traceback # traceback of last uncaught exception
    print("Good bye!")

sys.exitfunc=sayGoodbye

sayGoodbye()

sys.excepthook=myExcepthook

1/0



