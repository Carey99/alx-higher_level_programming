#!/usr/bin/python3
"""Defines a square while handling errors"""


class Square:
    """Attr descrptn starts here"""
    def __init__(self, size=0):
        """Args:
            Size: Must be int
        """
        self.size = size

    @property
    def size(self):
        """Setter"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square with '#' """
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
