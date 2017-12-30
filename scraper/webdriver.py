import os
from selenium import webdriver
from flask import current_app

PHANTOMJS_EXE_PATH = './node_modules/phantomjs-prebuilt/bin/phantomjs'
FIREFOX_EXE_PATH = './webdrivers/geckodriver'


class MyWebdriver:
    def __init__(self):
        if current_app.config['USE_FIREFOX']:
            self.browser = webdriver.Firefox(executable_path=FIREFOX_EXE_PATH)
        else:
            self.browser = webdriver.PhantomJS(executable_path=PHANTOMJS_EXE_PATH)
        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.browser.quit()
