#!/usr/bin/python3
from importlib import import_module

name_of_module = "variable_load_5"
var = "a"

if __name__ == "__main__":
    module = import_module(name_of_module)
    n = getattr(module, var)
    print("{}".format(n))
