#!/usr/bin/python3
"""JSON representation"""


import json


def to_json_string(my_obj):
    """
    Returns a JSON rep of obj
    """
    return json.dumps(my_obj)
