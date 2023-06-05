#!/usr/bin/python3

"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """Initializing the rectangle class"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):

        """retrieves width attribute"""

        return self.__width

    @width.setter
    def width(self, value):

        """sets width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """retrieves height attribute"""

        return self.__height

    @height.setter
    def height(self, value):

        """sets height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """returns the rectangle area"""

        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):

        """Returns a string representation of the rectangle"""

        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):

        """Returns a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):

        """Prints a message and decrements
        number_of_instances by 1 when rectangle
        instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):

        """Returns the biggest rectangle based on the area"""

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):

        """Class method to create a square rectangle"""

        return cls(size, size)
