#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except request.HTTPError as error:
        print("Erorr code: {}".format(error.code))
