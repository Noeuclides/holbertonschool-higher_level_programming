#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as r_file:
        print(r_file.read(), end='')
