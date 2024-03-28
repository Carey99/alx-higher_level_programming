#!/usr/bin/python3
"""Finds a peak in a list of unsorted int"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    mid_point = int(size / 2)
    peak = list_of_integers[mid_point]

    if peak > list_of_integers[mid_point - 1] and peak > list_of_integers[mid_point + 1]:
        return peak
    elif peak < list_of_integers[mid_point - 1]:
        return find_peak(list_of_integers[:mid_point])
    else:
        return find_peak(list_of_integers[mid_point + 1:])
