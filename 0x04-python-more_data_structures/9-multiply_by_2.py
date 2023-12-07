#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    product = {}
    for key, value in a_dictionary.items():
        product[key] = value * 2
    return product
