#!/usr/bin/python3
"""Flask web"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def tr_down(exception):
    """close session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    """list states"""
    all_state = storage.all("State")
    all_states = sorted(list(all_state.values()), key=lambda x: x.name)
    return render_template('7-states_list.html', all_states=all_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
