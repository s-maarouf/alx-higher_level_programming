#!/usr/bin/python3

"""Define matrix elements division"""


def matrix_divided(matrix, div):

    """A function that divides all elements of a matrix"""

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    for items in lists:
        if type(items) not in (int, float):
            raise TypeError('matrix must be a matrix (list of lists)\
            of integers/floats')
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
