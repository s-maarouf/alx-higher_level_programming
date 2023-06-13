#!/usr/bin/python3

"""Define saving args as a list to a file"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    try:
        data = load_from_json_file('add_item.json')

    except FileNotFoundError:

        data = []

    data.extend(sys.argv[1:])
    save_to_json_file(data, "add_item.json")
