#!/usr/bin/python3
def best_score(a_dictionary):
    a = a_dictionary
    if a is not None:
        n = len(a) - 1
        return(list(a.keys())[list(a.values()).index(sorted(a.values())[n])])
