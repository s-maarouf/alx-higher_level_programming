#!/usr/bin/python3

"""Define locked class"""


class LockedClass:

    """prevents the user from creating new instance
       attributes except if the new instance
       attribute is called first_name"""

    __slots__ = ["first_name"]
