#!/usr/bin/python3
"""Based on 6-base_geometry.py"""



class BaseGeometry:
    """
    Base cgeo definition
    """

    def area(self):
        """
        not implemented
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
