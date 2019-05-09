#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    sum = 0
    for x in a:
        sum += x
    return(sum)
