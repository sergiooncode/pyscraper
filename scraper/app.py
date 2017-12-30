import os
from flask import Flask

from scraper import Base

BASE_DIR = os.path.dirname(os.path.abspath(__name__))


def create_app():
    app = Flask(__name__)
    configure_app(app)
    return app


def configure_app(app):
    if os.environ.get('SCRAPER_SETTINGS'):
        app.config.from_envvar('SCRAPER_SETTINGS')
        return
    default_config_path = "{}{}".format(
        BASE_DIR,
        '/config/config-local.py'
    )
    app.config.from_pyfile(default_config_path)


def init_db():
    from scraper.models import Book
    Base.metadata.create_all()


def drop_db():
    from scraper.models import Book
    Base.metadata.drop_all()
