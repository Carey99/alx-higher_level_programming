#!/usr/bin/python3
"""Load, add, save"""


import sys
import os.path


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    file_path = "add_item.json"

    if os.path.isfile(file_path):
        items = load_from_json_file(file_path)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, file_path)
