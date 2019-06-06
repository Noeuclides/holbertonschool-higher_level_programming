#!/usr/bin/python3
def number_of_lines(filename=""):
    i = 0
    with open(filename, mode='r', encoding='utf-8') as r_file:
        for line in r_file:
            i += 1
        return(i)
