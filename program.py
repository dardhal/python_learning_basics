#!/usr/bin/python3
#
# First Python program
#

file_path = "/etc/services"
line = ""
nlines = 0

with open (file_path, "rt") as fh:
    line = fh.readline()
    while len(line) != 0: 
            nlines += 1
            line = fh.readline()
print (nlines)
