#!/usr/bin/python3
"""Module containing flask app"""
from flask import Flask

flaskApp = Flask(__name__)


@flaskApp.route("/", strict_slashes=False)
def helloHBNB():
    """Display hello HBNB"""
    return "Hello HBNB!"

if __name__ == "__main__":
    flaskApp.run(host="0.0.0.0", port=5000)

