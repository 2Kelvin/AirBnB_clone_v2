#!/usr/bin/python3
"""Module containing route c"""
from flask import Flask
from markupsafe import escape

flaskApp = Flask(__name__)


@flaskApp.route('/', strict_slashes=False)
def helloHBNB():
    """Display hello HBNB"""
    return 'Hello HBNB!'


@flaskApp.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@flaskApp.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """Displays route c"""
    spaceText = text.replace('_', ' ')
    return 'C {}'.format(escape(spaceText))


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)
