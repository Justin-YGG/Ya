# coding:utf-8

from flask import Flask
from werkzeug.utils import import_string

blueprints = [
    'sky.views.home:bp'
    ]


def create_app(config=None):

    app = Flask(__name__)
    app.config.from_object('envcfg.json.ya')
    app.config.from_object(config)

    for blueprint_qualname in blueprints:
        blueprint = import_string(blueprint_qualname)
        app.register_blueprint(blueprint)

    return app
