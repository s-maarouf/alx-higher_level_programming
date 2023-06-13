#!/usr/bin/python3

"""Define file appending function"""


def append_write(filename="", text=""):

    """function that appends a string to a text file (UTF8) and
    returns the number of characters written"""

    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return len(text)
