#!/usr/bin/python3
"""States and State module"""
from flask import Flask, render_template
from models import storage
from models.state import State


flaskApp = Flask(__name__)


@flaskApp.teardown_appcontext
def teardownSession(self):
    """Teardown method to remove the SQLAlchemy session"""
    storage.close()


@flaskApp.route('/states', strict_slashes=False)
def statesRoute():
    """Route to render states_list route"""
    dataStates = storage.all(State).values()
    return render_template('9-states.html', states=dataStates, spef='all')


@flaskApp.route('/states/<id>', strict_slashes=False)
def idStates(id):
    """Render a specific state using it's passed in id"""
    statesData = storage.all(State).values()
    for st in statesData:
        if st.id == id:
            return render_template('9-states.html', states=st, spef='id')
    return render_template('9-states.html', states=st, spef='none')


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)
