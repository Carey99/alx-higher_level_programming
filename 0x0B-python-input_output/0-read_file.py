#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """
    Reads UTF8 and prints to output
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
