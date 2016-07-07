# coding:utf-8

from flask_script import Manager

from sky.app import create_app
from sky.extensions import db

app = create_app()
manager = Manager(app)

@manager.command
def runserver(host=None, port=None, workers=None):
    host = host or app.config.get('HTTP_HOST') or '0.0.0.0'
    port = port or app.config.get('HTTP_PORT') or 5000
    workers = workers or app.config.get('HTTP_WORKERS') or 1
    use_evalex = app.config.get('USE_EVALEX', app.debug)

    if app.debug:
        app.run(host, int(port), use_evalex=use_evalex)


def main():
    manager.run()

if __name__ == '__main__':
    main()
