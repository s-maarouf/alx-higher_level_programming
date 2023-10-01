#!/usr/bin/python3
"""Takes your Github credentials (username and password) and uses the Github
    API to display your id"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    resp = requests.get(url, auth=(username, password))
    print(resp.json().get('id'))
