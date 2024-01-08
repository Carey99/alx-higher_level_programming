#!/usr/bin/python3
"""Checking if inherited directly or indirectly"""


def inherits_from(obj, a_class):
    """
    Returns true or false
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
