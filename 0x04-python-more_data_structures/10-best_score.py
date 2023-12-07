#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    big_k, big_v = next(iter(a_dictionary.items()))

    for key, value in a_dictionary.items():
        if value > big_v:
            big_k, big_v = key, value
    return big_k
