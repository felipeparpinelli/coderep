__author__ = 'Felipe Parpinelli'


class Component:
    name = ""
    stars = 0
    tags = 0
    rep = 0
    github_url = ""

    def __init__(self, name, stars, tags, github_url):
        self.name = name
        self.stars = stars
        self.tags = tags
        self.github_url = github_url
