#!/usr/bin/python3
def add(a, b):
    a = 1
    b = 2
    total = a + b
    print("{:d} + {:d} = {:d}".format(a, b, total))

    from add_0 import add
    add(1, 2)
