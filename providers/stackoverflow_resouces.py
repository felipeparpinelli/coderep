__author__ = 'Felipe Parpinelli'

import requests
import json
import simplejson
import urllib2


def auth():
    return 'OK'


def get_tags(comp):
    so_url = 'https://api.stackexchange.com/2.2/tags?site=stackoverflow&inname=%s' % comp
    count = 0

    try:
        r = requests.get(so_url)
        content = json.loads(r.content.decode('utf-8-sig'))
    except ValueError:
        raise
        pass

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