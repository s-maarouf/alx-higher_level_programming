#!/usr/bin/python3

"""Define MyList class"""


class MyList(list):

    def print_sorted(self):

        """Prints sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
