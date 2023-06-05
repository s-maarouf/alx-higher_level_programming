#!/usr/bin/python3

"""Define Rectangle class"""


class Rectangle:

    """Rectangle class"""

    def __init__(self, width=0, height=0):

        """Initialize a new Rectangle.

        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """

        self.__width__ = width
        self.__height__ = height

    @property
    def width(self):

        """retrieves the width of the rectangle."""

        return self.__width__

    @width.setter
    def width(self, value):
        """sets height attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """retrieves the height of the rectangle."""

        return self.__height__

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
