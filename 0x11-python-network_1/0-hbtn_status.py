#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""

from urllib import request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as response:
        body = response.read()
        to_print = f"Body response:\n\
    - type: {body.__class__}\n    - content: {body}\n\
    - utf8 content: {body.decode()}"
        print(to_print)
