#!/usr/bin/python3
def islower(c):
    """
    checks if a character is lowercase.

    Arg:
    c(str): Character to check.

    Returns:
    bool: True if lowercase else false.
    """
    if 'a' <= c <= 'z':
        return True
    else:
        return False
