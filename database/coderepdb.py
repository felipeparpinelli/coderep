__author__ = 'Felipe Parpinelli'

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from models.component import Component
from models.language import Language

engine = create_engine('mysql://root:rootroot@localhost/coderep?charset=utf8&use_unicode=0')

Session = sessionmaker()

Session.configure(bind=engine)

session = Session()

Base = declarative_base()

connection = engine.connect()


def insert_component(comp):

    try:
        session.add(comp)
        session.commit()
    except exc.IntegrityError:
        session.rollback()
        print 'This component already exist!'
    except:
        print 'Error when try to insert component in database'
        raise


def update_values(comp):
    session.query(Component).filter(Component.id == comp.id).update({'stars': comp.stars})
    session.query(Component).filter(Component.id == comp.id).update({'tags': comp.tags})
    session.query(Component).filter(Component.id == comp.id).update({'rep': comp.rep})
    session.commit()


def get_all_components():
    # force to get new values.
    session.commit()
    return session.query(Component).all()


def get_all_languages():
    return session.query(Language).all()