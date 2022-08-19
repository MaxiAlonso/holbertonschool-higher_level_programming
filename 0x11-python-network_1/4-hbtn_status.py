#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    body = requests.get(url).text
    to_print = "Body response:\n\t- type: {}\n\t- content: {}\
".format(type(body), body, body)
    print(to_print)
