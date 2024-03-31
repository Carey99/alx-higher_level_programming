#!/usr/bin/python3
"""Displays users GitHub id"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        print(data['id'])
