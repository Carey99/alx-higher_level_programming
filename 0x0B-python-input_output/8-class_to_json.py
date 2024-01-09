#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    Returns dict with list str etc
    """
    return obj.__dict__
