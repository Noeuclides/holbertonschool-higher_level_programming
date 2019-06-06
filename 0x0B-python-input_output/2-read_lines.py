#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    i = 0
    with open(filename, mode='r', encoding='utf-8') as r_file:
        for line in r_file:
            i += 1
        if nb_lines <= 0 or nb_lines >= i:
            r_file.seek(0)
            print(r_file.read(), end="")
        else:
            r_file.seek(0)
            for m in range(nb_lines):
                print(r_file.readline(), end="")
