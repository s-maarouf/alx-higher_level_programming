#!/usr/bin/python3

"""define base class"""


class Base:

    """initialise base class"""

    __nb_objects = 0

    def __init__(self, id=None):

        """manages id attribute"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
