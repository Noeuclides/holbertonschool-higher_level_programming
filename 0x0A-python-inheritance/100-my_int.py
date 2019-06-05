#!/usr/bin/python3


class MyInt(int):
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return(self.x != other)

    def __ne__(self, other):
        return(self.x == other)
