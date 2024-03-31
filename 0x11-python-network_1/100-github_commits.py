#!/usr/bin/python3
"""
    Lists commits from newest to oldest
    -repository --> "rails"
    -user --> "rails"
    -list sort from new to old
    -print("{}\n".format(data['commits']))
    -sys.argv[1] --> repository name
    -sys.argv[2] --> owner name
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        commits = data[:10]
        for commit in commits:
            sha = commit['sha']
            auth_name = commit['commit']['author']['name']
            print(f"{sha}: {auth_name}")
