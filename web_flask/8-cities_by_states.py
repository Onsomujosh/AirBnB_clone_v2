#!/usr/bin/python3
"""starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """returns html template at /cities_by_states route,
    listing cities by state."""
    states = storage.all(State).values()
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)
    return render_template('8-cities_by_states.html', states=states,
                            state_cities=cities)


@app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
