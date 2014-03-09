__author__ = 'Felipe Parpinelli'

from sqlalchemy import *

db = create_engine('mysql://root:rootroot@localhost/coderep?charset=utf8&use_unicode=0', 'pool_recycle=3600')

db.echo = False

connection = engine.connect()
