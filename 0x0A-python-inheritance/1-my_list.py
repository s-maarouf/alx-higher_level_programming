#!/usr/bin/python3

"""Define MyList class"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
