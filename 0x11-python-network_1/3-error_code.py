#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
    response (decoded in utf-8)."""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
