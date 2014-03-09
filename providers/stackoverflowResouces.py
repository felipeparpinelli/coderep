__author__ = 'Felipe Parpinelli'

import requests
import json


def auth():
    return 'OK'


def getTags(comp):
    mockUrl = 'http://api.stackoverflow.com/1.1/tags?filter=%s' % comp
    r = requests.get(mockUrl)

    repoItem = json.loads(r.content)
    tags = list(repoItem['tags'])

    for tag in tags:
        if tag['name'] == comp:
            count = tag['count']

    return count