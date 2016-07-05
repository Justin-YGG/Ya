# coding: utf-8

from werkzeug.contrib.fixers import ProxyFix

from sky.app import create_app

#: WSGI endpoint
app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
