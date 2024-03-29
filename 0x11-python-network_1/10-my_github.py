#!/usr/bin/python3
"""Display GitHub user id using Basic Authentication"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    try:
        response = requests.get(url, auth=(username, password))
        response.raise_for_status()

        user_data = response.json()

        print("User ID:", user_data['id'])
    except requests.exceptions.RequestException as e:
        print("Error:", e)
