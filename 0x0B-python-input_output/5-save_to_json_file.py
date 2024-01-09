#!/usr/bin/python3
"""Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an obj to txt file
    Obj is json representantion
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
