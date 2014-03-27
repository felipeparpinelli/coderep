__author__ = 'Felipe Parpinelli'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('mysql://root:rootroot@localhost/coderep?charset=utf8&use_unicode=0')

Base = declarative_base()


class Component(Base):
    __tablename__ = 'components'

    id = Column(Integer)
    name = Column(String, primary_key=True)
    stars = Column(Integer)
    tags = Column(Integer)
    rep = Column(Integer)
    github_url = Column(String)

    def __init__(self, name, stars, tags, rep, github_url):
        self.name = name
        self.stars = stars
        self.tags = tags
        self.rep = rep
        self.github_url = github_url

    def __repr__(self):
        return "<components(name='%s', stars='%d', tags='%d', rep='%d', github_url='%s')>" % (
            self.name, self.stars, self.tags, self.rep, self.github_url)




