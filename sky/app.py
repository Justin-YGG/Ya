# coding:utf-8

from flask import Flask
from werkzeug.utils import import_string


blueprints = [
    'sky.views.home:bp'
    ]

extensions = [
    'sky.extensions:db',
    'sky.extensions:cache'
    ]


def create_app(config=None):

    config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'fcache',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': '6379',
    'CACHE_REDIS_URL': 'redis://localhost:6379'
    }
    app = Flask(__name__)
    app.config.from_pyfile('app.cfg')
    app.config.from_object('envcfg.json.ya')
    app.config.from_object(config)

    for blueprint_qualname in blueprints:
        blueprint = import_string(blueprint_qualname)
        app.register_blueprint(blueprint)

    for extension_qualname in extensions:
        extension = import_string(extension_qualname)
        extension.init_app(app)

    return app
