#!/usr/bin/python3
def roman_to_int(roman_string):
    if len(roman_string) == 0:
        return(0)
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = list(roman_string)
    num = 0
    a = 1
    for i in range(len(r)-1):
        if r[i] not in romans:
            return(0)
        elif romans[r[i]] >= romans[r[i + 1]]:
            num += romans[r[i]]
            a = 1
        else:
            sub = romans[r[i+1]] - romans[r[i]]
            num += sub
            a = 0
            i += 1
    if a == 0:
        return(num)
    return(num + romans[r[len(r)-1]])
