#!/usr/bin/python3
"""
module that has
a function
that prints full name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints first and last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("first_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
