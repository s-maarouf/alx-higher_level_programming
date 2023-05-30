#!/usr/bin/python3

"""define a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args: size of square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns square area"""
        return (self.__size * self.__size)
