#!/usr/bin/python3
"""
module that
checks if an object
is and instance of a class
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly instance of the class
    """
    return(type(obj) is a_class)
