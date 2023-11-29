#!/usr/bin/python3
start = ord('a')
end = ord('{')

mystr = "".join(chr(i) for i in range(start, end))
for i, char in enumerate(mystr[::-1]):
    toggle = char.lower() if i % 2 == 0 else char.upper()
    print("{}".format(toggle), end="")
print()
