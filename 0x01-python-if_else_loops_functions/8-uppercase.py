#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) < 123 and ord(i) > 96:
            j = ord(i) - 32
            i = chr(j)
        print("{:c}".format(ord(i)), end="")
    print()
