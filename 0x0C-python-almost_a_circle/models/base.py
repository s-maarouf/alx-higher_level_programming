#!/usr/bin/python3

"""define base class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):

        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):

        """returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            pass
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):

        """opens a window and draws all the Rectangles
        and Squares using turtle GUI"""

        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(0)
        pen.width(2)
        pen.color("#E7CEA6")

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.width)
                pen.left(90)

        turtle.done()
