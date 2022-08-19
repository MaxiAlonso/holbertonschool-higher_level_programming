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
        to_print = "Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".format(body.__class__, body, body.decode())
        print(to_print)
