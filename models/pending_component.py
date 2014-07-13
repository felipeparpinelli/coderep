__author__ = 'Felipe Parpinelli'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PendingComponent(Base):
    __tablename__ = 'pendingComponent'

    name = Column(String, primary_key=True)
    stars = Column(Integer)
    tags = Column(Integer)
    rep = Column(Integer)
    github_url = Column(String)
    language_id = Column(Integer)

    def __init__(self, name, stars, tags, rep, github_url, language_id):
        self.name = name
        self.stars = stars
        self.tags = tags
        self.rep = rep
        self.github_url = github_url
        self.language_id = language_id

    def __repr__(self):
        return "<pendingComponent(name='%s', stars='%d', tags='%d', rep='%d', github_url='%s', language_id='%d')>" % (
            self.name, self.stars, self.tags, self.rep, self.github_url, self.language_id)