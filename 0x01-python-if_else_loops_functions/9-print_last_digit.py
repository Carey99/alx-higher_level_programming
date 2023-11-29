#!/usr/bin/python3
def print_last_digit(number):
    result = ""
    for i in str(number):
        if i == str(number)[-1]:
            result += i
            print("{}".format(result), end="")
            return result
