#!/usr/bin/python3

"""Define an int addition"""


def add_integer(a, b=98):

    """A fucntion that adds 2 integers"""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + b)
