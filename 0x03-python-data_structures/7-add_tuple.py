#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    if len(tuple_a) == 0:	
        add_t = [b[0], b[1]]
    if len(tuple_b) == 0:
        add_t = [a[0] + 0, a[1] + 0] 
    if len(tuple_a) == 1:
        add_t = [b[0], a[0] + b[1]]
    if len(tuple_b) == 1:
        add_t = [a[0] + a[0], a[1]] 
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        add_t = [a[0] + b[0], a[1] + b[1]]
    return(tuple(add_t))
