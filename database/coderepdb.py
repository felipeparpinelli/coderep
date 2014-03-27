__author__ = 'Felipe Parpinelli'

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from models.component import Component

engine = create_engine('mysql://root:rootroot@localhost/coderep?charset=utf8&use_unicode=0')

Session = sessionmaker()

Session.configure(bind=engine)

session = Session()

Base = declarative_base()

connection = engine.connect()


def insertComponent(comp):

    try:
        session.add(comp)
        session.commit()
    except exc.IntegrityError:
        session.rollback()
        print 'This component already exist!'
    except:
        print 'Error when try to insert component in database'
        raise


def checkComponent(components):
    q = session.query(components).filter_by(components.name == 'felipe')
    if session.query(q.exists()):
        return true
    return false


def getAllComponents():
    return session.query(Component).all()
