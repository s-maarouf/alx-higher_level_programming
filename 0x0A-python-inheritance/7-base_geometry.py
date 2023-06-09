#!/usr/bin/python3

"""Define BaseGeometry class"""


class BaseGeometry:

    """BaseGeometry class"""

    def area(self):

        """raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """validates value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
