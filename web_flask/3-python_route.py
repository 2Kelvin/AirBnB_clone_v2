#!/usr/bin/python3
"""Module containing route python"""
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


@flaskApp.route('/python/<text>', strict_slashes=False)
@flaskApp.route('/python', strict_slashes=False)
def pythonIsCool(text='is cool'):
    """Displays route python"""
    if text:
        text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)
