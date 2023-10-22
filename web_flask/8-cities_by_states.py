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


@flaskApp.route('/states_list', strict_slashes=False)
def statesList():
    """Route to render states list"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', allStates=states)


@flaskApp.route('/cities_by_states', strict_slashes=False)
def citiesDisplayed():
    """Route to render states list"""
    dataStates = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=dataStates)


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)
