#!/usr/bin/python3
"""
module that
checks if an object is
a subclass of
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
 that inherited (directly or indirectly) from the specified class ;
 otherwise False.
    """
    return(isinstance(obj, a_class))
