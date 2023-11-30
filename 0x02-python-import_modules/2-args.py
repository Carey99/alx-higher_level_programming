#!/usr/bin/python3
import sys


def print_arguments():

    length = len(sys.argv)
    i = 1
    argnum = length - 1
    if length == 1:
        print("{} arguments.".format(argnum))
    elif length == 2:
        print("{} argument:".format(argnum))
    elif length > 1:
        print("{} arguments:".format(argnum))
    while i < length:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

if __name__ == "__main__":

    print_arguments()
