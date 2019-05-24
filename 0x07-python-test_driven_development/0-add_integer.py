#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        return(int(a) + int(b))
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")
