#!/usr/bin/python3
"""
module that
checks if an object
is the same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
     function that returns True if the object is an instance of a class.
    """
    return(isinstance(obj, a_class))
