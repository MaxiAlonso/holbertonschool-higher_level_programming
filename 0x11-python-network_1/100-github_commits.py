#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
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
    for element in dic:
        str = "{}".format(element.get('sha'))
        str += " {}".format(element.get('commit').get('author').get('name'))
        new_list.append(str)
    for i in range(10):
        print(new_list[i])
