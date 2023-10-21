#!/usr/bin/python3
"""Module contains a cities template rendered by Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State


flaskApp = Flask(__name__)


@flaskApp.teardown_appcontext
def teardownSession(self):
    """Teardown method to remove the SQLAlchemy session"""
    storage.close()


@flaskApp.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Route to render states list"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)
