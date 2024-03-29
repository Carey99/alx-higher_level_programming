#!/usr/bin/python3
"""Handle errors"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        r = requests.get(url)

        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Error code", r.status_code)
