#!/usr/bin/python3
"""
module that  has
functions with list
inheritance
"""


class MyList(list):
    """
    prints sorted list
    """
    def print_sorted(self):
        print(sorted(self))
