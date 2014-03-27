__author__ = 'Felipe Parpinelli'

import requests
import json
import database.coderepdb
from models.component import Component


def auth():
    return 'OK'


def getStars(url):
    r = requests.get(url)

    repoItem = json.loads(r.content)
    stars = str(repoItem['stargazers_count'])
    print "Component stars: " + stars

    comp = Component("felipe", int(stars), 4331, 1, "hard coder")

    database.coderepdb.insertComponent(comp)

    return stars


