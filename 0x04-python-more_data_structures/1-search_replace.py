#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for x in new_list:
        r = map(lambda x: replace if x == search else x, new_list)
    return(list(r))
