#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman_numerals = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    total = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string):
            next_char = roman_string[i + 1].lower()
            next_value = roman_numerals[next_char]
            if next_value > current_value:
                total += next_value - current_value
                i += 2
            else:
                total += current_value
                i += 1
    return total
