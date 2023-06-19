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

    @property
    def width(self):
        """returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """checks for rectangle width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """checks for rectangle height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x coordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        """checks for x coordinates value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y coordinates"""
        return self.__y

    @y.setter
    def y(self, value):
        """checks for y coordinates value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns rectangle's area"""
        return (self.__width * self.__height)

    def display(self):
        """Display the Rectangle instance with '#' character"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return string representation of Rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            self.__id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
