#!/usr/bin/python3
#
# First Python program
#

file_path = "/etc/services"
print ("Hello World!")
line = ""
nlines = 0
err = False

with open (file_path, "rt") as fh:
    while err != True: 
        line = fh.readline()
        if len(line) > 0:
            err = False
            nlines += 1
        else:
            err = True

print (nlines)

