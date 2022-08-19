#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    value = ""
    if len(argv) != 1:
        value = argv[1]
    values = {'q': value}
    response = requests.post(url, data=values)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get("id"),
                  json_response.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
