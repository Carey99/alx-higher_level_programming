#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newM = []
    for i in range(len(matrix)):
        newM += [list(map(lambda x: x ** 2, matrix[i]))]
    return newM
