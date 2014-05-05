__author__ = 'Felipe Parpinelli'

import requests
import json
import database.coderepdb
from models.component import Component
from urlparse import urlparse
import settings


def auth():
    return 'OK'


def get_stars(url):
    r = requests.get(url, auth=(settings.GH_USERNAME, settings.GH_PWD))

    content = json.loads(r.content)
    stars = str(content['stargazers_count'])
    print "Component stars: " + stars

    #comp = Component("felipe", int(stars), 4331, 1, "hard coder")

    #database.coderepdb.insert_component(comp)

    return stars


def check_valid(url):

    url = urlparse(url, 'https', True)

    if url.hostname == 'github.com' and url.scheme == 'https':
        return True

    return False

