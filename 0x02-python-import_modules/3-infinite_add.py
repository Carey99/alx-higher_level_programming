#!/usr/bin/python3
import sys


def infinite_add():
    i = 1
    total = 0
    length = len(sys.argv)

    while i < length:
        total += int(sys.argv[i])
        i += 1
    print("{}".format(total))


if __name__ == "__main__":
    infinite_add()
