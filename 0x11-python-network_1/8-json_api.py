#!/usr/bin/python3
"""Takes a letter a sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    try:
        response = requests.post(url, data=data)

        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except ValueError:
        print("Not a valid JSON")
