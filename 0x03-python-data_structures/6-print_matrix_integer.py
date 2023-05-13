#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, element in enumerate(row):
            if i != len(row) - 1:
                print(element, end=' ')
            else:
                print(element, end='')
        print()
