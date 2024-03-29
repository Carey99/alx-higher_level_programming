#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """
    Defdines student based on 9-student.py
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a dict rep
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
