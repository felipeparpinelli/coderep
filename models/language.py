__author__ = 'Felipe Parpinelli'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('mysql://root:rootroot@localhost/coderep?charset=utf8&use_unicode=0')

Base = declarative_base()


class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<components(id='%d', name='%s')>" % (
            self.id, self.name)




