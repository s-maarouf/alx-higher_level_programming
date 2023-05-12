#!/usr/bin/python3

def no_c(my_string):
    if 'c' in my_string or 'C' in my_string:
        my_string = ''.join([c for c in my_string if c.lower() != 'c'])
        my_string = ''.join([C for C in my_string if C != 'C'])
        return my_string
