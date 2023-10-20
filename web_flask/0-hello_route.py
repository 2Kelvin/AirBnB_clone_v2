#!/usr/bin/python3
"""Contains route /"""
from web_flask import createFlaskApp

flaskApp = createFlaskApp()


@flaskApp.route('/', strict_slashes=False)
def helloHBNB():
    """Route / to display hello HBNB"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)

