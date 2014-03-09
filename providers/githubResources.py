__author__ = 'Felipe Parpinelli'

import requests
import json


def auth():
    return 'OK'


def getStars(url):
    r = requests.get(url)

    repoItem = json.loads(r.content)
    stars = str(repoItem['stargazers_count'])
    print "Component stars: " + stars

    return stars