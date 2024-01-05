#!/usr/bin/python3
"""My class"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    except when called firstname
    """

    __slots__ = 'first_name'
