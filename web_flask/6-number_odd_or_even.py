#!/usr/bin/python3
"""Module containing odd or even number template"""
from flask import Flask
from markupsafe import escape
from flask import render_template

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


@flaskApp.route('/number/<int:n>', strict_slashes=False)
def numberN(n):
    """Display only numbers"""
    return '{} is a number'.format(n)


@flaskApp.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """Render a number template"""
    return render_template('5-number.html', num=n)


@flaskApp.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberOddOrEvenTemplate(n):
    """Template to render an even or odd number"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)
