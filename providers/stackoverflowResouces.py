__author__ = 'Felipe Parpinelli'

import requests
import json


def stackoverflowTest():
    mockUrl = 'http://api.stackoverflow.com/1.1/tags?filter=django'
    r = requests.get(mockUrl)

    repoItem = json.loads(r.content)

    for tag in repoItem.tags:
        print tag


    return 'OK'