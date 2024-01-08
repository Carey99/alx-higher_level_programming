#!/usr/bin/python3
""" returns True if the object is exactly"""


def is_same_class(obj, a_class):
    """
    Return True if object  is of specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
