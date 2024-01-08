#!/usr/bin/python3
"""Checking if inherited directly or indirectly"""

def inherits_from(obj, a_class):
    """
    Returns true or false
    """
    return isinstance(obj, a_class) and type(obj) != a_class
