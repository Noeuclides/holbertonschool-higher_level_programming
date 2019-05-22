#!/usr/bin/python3
class Node:
    def __init__(self, data=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def data(self):
        return(self.__size ** 2)
    def data(self, value):

