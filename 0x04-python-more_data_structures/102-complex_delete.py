#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d = a_dictionary
    for key, val in list(d.items()):
        if val == value:
            del d[key]
    return(d)
