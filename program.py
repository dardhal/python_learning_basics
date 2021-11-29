#!/usr/bin/python3
#
# First Python program
#

file_path = "/etc/services"

def count_file_lines(file_path):
    nlines = 0
    with open(file_path, "rt") as fh:
        line = fh.readline()
        while len(line) != 0:
            nlines += 1
            line = fh.readline()
        print(f"File {file_path} is {nlines} lines long")
        return nlines

count_file_lines("/etc/services")
count_file_lines("/etc/protocols")
count_file_lines("/etc/shadow")
