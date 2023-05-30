#!/usr/bin/python3

"""define a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args: size of square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
