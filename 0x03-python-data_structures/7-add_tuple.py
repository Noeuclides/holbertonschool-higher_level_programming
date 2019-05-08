#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        add_t = [0, 0]
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        add_t = [a[0] + b[0], 0]
    elif len(tuple_a) == 0:
        add_t = [b[0], b[1]]
    elif len(tuple_b) == 0:
        add_t = [a[0] + 0, a[1] + 0]
    elif len(tuple_a) == 1:
        add_t = [b[0], a[0] + b[1]]
    elif len(tuple_b) == 1:
        add_t = [a[0] + a[0], a[1]]
    else:
        add_t = [a[0] + b[0], a[1] + b[1]]
    return(tuple(add_t))
