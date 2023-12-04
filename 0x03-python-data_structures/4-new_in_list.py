#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(copied_list)):
        if i == idx:
            copied_list[i] = element
            return copied_list
