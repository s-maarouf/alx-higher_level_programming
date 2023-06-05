#!/usr/bin/python3

"""Define Rectangle class"""


class Rectangle:

    """Rectangle class"""

    def __init__(self, width=0, height=0):

        """Sets rectangle width"""

        self.__width__ = width
        self.__height__ = height

    @property
    def width(self):
        return self.__width__

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height__

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
