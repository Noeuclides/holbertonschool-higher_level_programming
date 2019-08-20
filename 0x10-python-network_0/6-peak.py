#!/usr/bin/python3

def find_peak(list_of_integers):
    list = list_of_integers
    if len(list) == 0:
        return None

    peak = list[0]

    for i in range(1, len(list) - 1):
        if list[i] > list[i - 1] and list[i] > list[i + 1]:
            peak = list[i]
    return(peak)

if __name__ == "__main__":
    find_peak()

