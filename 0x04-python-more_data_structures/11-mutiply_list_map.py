#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    new = my_list[:]
    return(list(map(lambda x: x*number, new)))
