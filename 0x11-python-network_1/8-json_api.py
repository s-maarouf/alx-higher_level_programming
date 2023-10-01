#!/usr/bin/python3
"""Takes in a letter and sends a POST request with the letter as a parameter"""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}
    resp = requests.post(url, data)
    try:
        json = resp.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
