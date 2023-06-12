#!/usr/bin/python3

"""Define MyInt"""


class MyInt(int):

    """MyInt has == and != operators inverted"""

    def __eq__(self, value):

        """Inverts == operator to !="""
        return self.real != value

    def __ne__(self, value):

        """Inverts != operator to =="""
        return self.real == value
