#!/usr/bin/python3

"""Define a function that prints a square with the character #"""


def print_square(size):

    """A fucntion  that prints a square with the character #"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
