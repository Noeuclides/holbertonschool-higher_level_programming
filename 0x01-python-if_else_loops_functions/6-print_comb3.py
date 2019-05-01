#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        elif i < j:
            print("{}{}, ".format(i, j), end="")
