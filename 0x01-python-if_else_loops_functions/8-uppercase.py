#!/usr/bin/python3
def uppercase(str):
    """

    Prints string in uppercase.

    Arg:
    c (str): String  to check.
    """
    result = ""
    for i in str:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    print("{}".format(result))
