#!/usr/bin/python3

"""Define file reading function"""


def read_file(filename=""):

    """function that reads a text file (UTF8) and prints it to stdout"""

    file = open(filename, 'r')
    content = file.read()
    print(content)
