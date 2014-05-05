__author__ = 'Felipe Parpinelli'

import requests
import json


def auth():
    return 'OK'


def get_tags(comp):
    so_url = 'http://api.stackoverflow.com/1.1/tags?filter=%s' % comp
    r = requests.get(so_url)
    count = 0

    content = json.loads(r.content)
    tags = list(content['tags'])

    for tag in tags:
        if tag['name'] == comp:
            count = tag['count']

    return count


def check_valid(url):
    req = requests.get(url)
    content = json.loads(req.content)
    tags = list(content['tags'])

    if req.status_code != 200 or len(tags) == 0:
        return False

    return True