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

