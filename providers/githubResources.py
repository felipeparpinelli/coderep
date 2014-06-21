__author__ = 'Felipe Parpinelli'

import requests
import json
import database.coderepdb
from models.component import Component
from urlparse import urlparse
import settings

lang = ''


def auth():
    return 'OK'


def get_stars(url):

    try:
        stars = ''
        r = requests.get(url, auth=(settings.GH_USERNAME, settings.GH_PWD))
        content = json.loads(r.content)
        stars = str(content['stargazers_count'])
        global lang
        lang = str(content['language'])
    except:
        pass

    print "Component stars: " + stars

    if stars is '':
        return 'error'

    #database.coderepdb.insert_component(comp)

    return stars


def check_valid(url):

    url = urlparse(url, 'https', True)

    if url.hostname == 'github.com' and url.scheme == 'https':
        return True

    return False

