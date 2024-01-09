#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        ptr = [1]

        for item in range(len(tri) - 1):
            ptr.append(tri[item] + tri[item + 1])
        ptr.append(1)
        triangles.append(ptr)
    return triangles
