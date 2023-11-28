#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = str(number)
if int(new[-1]) > 5:
    if number < 0:
        int(new[-1]) = -int(new[-1])
    print(f"Last digit of {number} is {new[-1]} and is greater than 5")
elif int(new[-1]) == 0:
    print(f"Last digit of {number} is {new[-1]} and is 0")
elif int(new[-1]) < 6 and not 0:
    print(f"Last digit of {number} is {new[-1]} and is less than 6 and not 0")
