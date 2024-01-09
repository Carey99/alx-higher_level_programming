#!/usr/bin/python3
"""Appends a str to the end of the file"""


def append_write(filename="", text=""):
    """
    Returns the number of char added
    """
    with open(filename, 'a') as f:
        f.write(text)
        return len(text)
