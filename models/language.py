__author__ = 'Felipe Parpinelli'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import database
import json

Base = declarative_base()


class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gh_count = Column(Integer)
    tags = Column(Integer)

    def __init__(self, id, name, gh_count, tags):
        self.id = id
        self.name = name
        self.gh_count = gh_count
        self.tags = tags

    def __repr__(self):
        return "<components(id='%d', name='%s', gh_count='%d', tags='%d')>" % (
            self.id, self.name, self.gh_count, self.tags)


def generate_json_languages():
    languages = database.coderepdb.get_all_languages()
    arrayText = []
    arraySize = []

    for language in languages:
        arrayText.append(language.name)
        result = (language.gh_count + language.tags) / 30000
        if result < 10:
            result = 12
        arraySize.append(int(result))

    array = [arrayText, arraySize]
    json_array = json.dumps(array)
    return json_array

