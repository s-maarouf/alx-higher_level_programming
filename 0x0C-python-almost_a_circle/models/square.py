#!/usr/bin/python3

"""Define Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):

        """initialise Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """return Square size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
