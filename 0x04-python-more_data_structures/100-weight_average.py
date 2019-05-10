#!/usr/bin/python3
def weight_average(my_list=[]):
    l = my_list
    if len(l) == 0:
        return(0)
    p, m = 0, 1
    new = []
    for j in range(len(l)):
        p = p + l[j][1]
    for i in range(len(l)):
        for j in range(len(l[i])):
            m = m * l[i][j]
        new.append(m)
        m = 1
    f = 0
    for a in new:
        f = f + a
    avg = f / p
    return(avg)
