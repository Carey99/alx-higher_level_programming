#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """
    defines students by various attr
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        _json
        """
        return self.__dict__
