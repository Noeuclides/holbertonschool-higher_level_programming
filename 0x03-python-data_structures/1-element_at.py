#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return(0)
    elif len(my_list) < idx - 1:
        return(0)
    else:
        return(my_list[idx])
