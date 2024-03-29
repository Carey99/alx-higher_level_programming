#!/usr/bin/python3
"""Displays value of X-Request-Id in header"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read()

        x_req_id = response.headers.get('X-Request-Id')
        print(x_req_id)
