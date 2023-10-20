"""Flask application factory"""
from flask import Flask


def createFlaskApp():
    """Flask application factory function:
      Initiates a flask app
    """
    app = Flask(__name__)
    return app
