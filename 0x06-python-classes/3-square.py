#!/usr/bin/python3
"""Defines a square while handling errors"""


class Square:
    """Attr descrptn starts here"""
    def __init__(self, size=0):
        """Args:
            Size: Must be int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of square"""
        return (self.__size ** 2)
