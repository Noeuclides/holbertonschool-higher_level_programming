#!/usr/bin/python3 
def say_my_name(first_name, last_name=""):
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except TypeError:
        raise TypeError("first_name must be a string")
    except TypeError:
        raise TypeError("first_name must be a string")
