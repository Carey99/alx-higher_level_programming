#!/usr/bin/python3
"""Displays users GitHub id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        data = response.json()
        print(data['id'])
