#!/usr/bin/python3
'''find the peak
'''


def find_peak(list_of_integers):
    '''method to find the peak in a list
    '''
    list = list_of_integers
    if len(list) == 0:
        return None

    peak = peak_func(list, int(len(list) / 2))
    return (peak)


def peak_func(list, i):
    '''aux function
    '''
    if i == 0 and len(list) > 1:
        print("i = 0", list)
        if list[i] >= list[i + 1]:
            return (list[i])
    elif i == len(list) - 1 and len(list) > 1:
        if list[i] >= list[i - 1]:
            return (list[i])
    elif len(list) > 1:
        if list[i] > list[i - 1] and list[i] > list[i + 1]:
            return (list[i])
    else:
        return(list[i])
    if list[i - 1] > list[i]:
        new_list = list[:i]
    else:
        new_list = list[i:]
    peak = peak_func(new_list, int(len(new_list) / 2))
    return (peak)


if __name__ == "__main__":
    find_peak()
