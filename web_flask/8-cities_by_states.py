#!/usr/bin/python3
"""flask"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tr_down(exception):
    """close session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def all_states_city():
    """route cities by states"""
    all_states = storage.all("State").values()
    return render_template('8-cities_by_states.html', all_states=all_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
