#!/usr/bin/python3

"""Define rectangle class"""

from models.base import Base

class Rectangle(Base):

    """Initialise rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """sets width and height of rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
