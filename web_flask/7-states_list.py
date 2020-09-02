#!/usr/bin/python3
"""Flask web"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tr_down():
    """close session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    """list states"""
    all_states = storage.all("State")
    all_states.sort()
    return render_template('7-states_list.html', all_states=all_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
