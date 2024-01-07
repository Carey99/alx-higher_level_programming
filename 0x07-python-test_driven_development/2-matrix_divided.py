#!/usr/bin/python
"""Divides matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div and round to 2 decimal places.

    Args:
    - matrix: a list of lists of integers or floats
    - div: a number (integer or float)

    Returns:
    - new_matrix: a new matrix with elements rounded to 2 decimal places
    """
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
