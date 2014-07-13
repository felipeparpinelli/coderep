__author__ = 'Felipe Parpinelli'

import os
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
GH_USERNAME = 'xxxxxxxxxx'
GH_PWD = 'xxxxxxxxxxxx'
REDIS_URI = 'localhost'

