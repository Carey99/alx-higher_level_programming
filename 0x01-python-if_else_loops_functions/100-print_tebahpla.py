#!/usr/bin/python3
mystr = "abcdefghijklmnopqrstuvwxyz"

for i, char in enumerate(mystr[::-1]):
    toggle = char.lower() if i % 2 == 0 else char.upper()
    print("{}".format(toggle), end="")
print()
