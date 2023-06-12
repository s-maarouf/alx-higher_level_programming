#!/usr/bin/python3

"""Define MyList class"""


class MyList(list):

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):

        """Prints sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
