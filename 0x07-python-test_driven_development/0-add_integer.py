#!/usr/bin/python3
"""Adds two int values"""


def add_integer(a, b=98):
    """
    Returns: Int and b
    Typecast and converts float int int before addition
    Raise TypeError if not int or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
