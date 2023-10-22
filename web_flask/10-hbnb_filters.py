#!/usr/bin/python3
"""HBNB filters task module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


flaskApp = Flask(__name__)


@flaskApp.teardown_appcontext
def teardownSession(self):
    """Teardown method to remove the SQLAlchemy session"""
    storage.close()


@flaskApp.route('/hbnb_filters', strict_slashes=False)
def citiesDisplayed():
    """Route to render states_list route"""
    stateData = storage.all(State).values()
    amenityData = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html',
        states=stateData,
        amenities=amenityData
    )


if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000)
