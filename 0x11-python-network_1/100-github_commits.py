#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
    response = requests.get(url)
    dic = response.json()
    new_list = []
    for element in dic[0:10]:
        print("{}: {}".format(element.get('sha'),
              element.get('commit').get('author').get('name')))
