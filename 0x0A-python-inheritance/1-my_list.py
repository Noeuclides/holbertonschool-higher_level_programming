#!/usr/bin/python3
class list:
    def __init__(self, list=[]):
        self.list = list

    def print_sorted(self):
        print(sorted(self.list))

    def append(self, num):
        self.list.append(num)
        return(self.list)

class MyList(list):
    pass
