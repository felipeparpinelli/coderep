__author__ = 'Felipe Parpinelli'

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import json
import database


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
    language_id = Column(Integer)

    def __init__(self, name, stars, tags, rep, github_url, language_id):
        self.name = name
        self.stars = stars
        self.tags = tags
        self.rep = rep
        self.github_url = github_url
        self.language_id = language_id

    def __repr__(self):
        return "<components(name='%s', stars='%d', tags='%d', rep='%d', github_url='%s', language_id='%d')>" % (
            self.name, self.stars, self.tags, self.rep, self.github_url, self.language_id)


def generate_json_components():
    components = database.coderepdb.get_all_components()
    languages = database.coderepdb.get_all_languages()

    key_name = "name"
    value_name = "components"

    key_children = "children"
    children = []

    key_size = "size"

    array = []

    for language in languages:
        for component in components:
            if language.id == component.language_id:
                comp_dict = {key_name: component.name, key_size: component.rep}
                array.append(comp_dict)

        mutable_dict = {key_name: language.name, key_children: array}
        children.append(mutable_dict)
        array = []

    dict = {key_name: value_name, key_children: children}
    dict = json.dumps(dict, ensure_ascii=False)
    global comp
    comp = dict

    return dict



