__author__ = 'Felipe Parpinelli'

import requests
import json


def auth():
    return 'OK'


def get_tags(comp):
    so_url = 'http://api.stackexchange.com/2.2/tags?site=stackoverflow&inname=%s' % comp
    r = requests.get(so_url)
    count = 0

    content = json.loads(r.content)
    items = list(content['items'])

    for item in items:
        if item['name'] == comp:
            count = item['count']

    return count


def check_valid(url):
    req = requests.get(url)
    content = json.loads(req.content)
    tags = list(content['tags'])

    if req.status_code != 200 or len(tags) == 0:
        return False

    return True