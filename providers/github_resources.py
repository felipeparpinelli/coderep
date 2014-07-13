__author__ = 'Felipe Parpinelli'

import requests
import json
from urlparse import urlparse
import settings
from database import coderepdb

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

    return stars


def check_valid(url):

    url = urlparse(url, 'https', True)

    if url.hostname == 'github.com' and url.scheme == 'https':
        return True

    return False


def get_repo_name(url):

    if check_valid(url):
        splited = url.split('/')
        return splited[4]

    return None


def update_stars():
    components = coderepdb.get_all_components()

    for component in components:
        url = component.github_url
        if url is not None:
            url_parse_api = url.replace("https://github.com/", "https://api.github.com/repos/")
            stars = get_stars(url_parse_api)
            if str(component.stars) != stars:
                component.stars = stars
                coderepdb.update_values(component)
    return 'ok'

