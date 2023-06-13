#!/usr/bin/python3

"""Define file reading function"""


def read_file(filename=""):

    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, 'r') as file:
        content = file.read()
    print(content)
