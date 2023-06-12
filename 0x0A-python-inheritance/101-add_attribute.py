#!/usr/bin/python3

"""Define attribute setter"""


def add_attribute(obj, att, value):

    """a function that adds a new attribute to an object if it’s possible"""

    if not hasattr(obj, "__dict__"):

        """Checks if object has attribute"""

        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
