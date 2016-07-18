# coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
from flask_seasurf import SeaSurf


db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'redis'})
seasurf = SeaSurf()
