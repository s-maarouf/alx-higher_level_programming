#!/usr/bin/python3

"""Define square area"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Square class"""

    def __init__(self, size):

        """Checks for size to be int"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
