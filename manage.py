#!/usr/bin/env python
from flask_script import Manager

from scraper.app import create_app
from scraper import db
from scraper.scraping import go_scrape, store

app = create_app()
manager = Manager(app)


@manager.shell
def make_shell_context():
    return {'app': app, 'db': db}


@manager.command
def scrape_and_store():
    books = go_scrape()
    store(books)


if __name__ == '__main__':
    manager.run()
