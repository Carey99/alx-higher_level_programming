#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Returns numbe r of chr written
    """
    with open(filename, 'w') as f:
        return f.write(text)
