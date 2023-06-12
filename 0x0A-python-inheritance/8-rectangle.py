#!/usr/bin/python3

"""Define Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Inheritance based on BaseGeometry"""

    def __init__(self, width, height):

        """Private instant that validates width and height to be int"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
