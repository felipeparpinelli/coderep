__author__ = 'Felipe Parpinelli'

import requests
import json

def githubTest():
    mockUrl = 'https://api.github.com/repos/django/django'
    r = requests.get(mockUrl)

    repoItem = json.loads(r.content)
    stars = str(repoItem['stargazers_count'])
    print "Django stars: " + stars

    return 'OK'