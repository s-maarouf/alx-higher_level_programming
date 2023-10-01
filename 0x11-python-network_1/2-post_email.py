#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the
    email as a parameter, and displays the body of the response (decoded in
    utf-8)"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
