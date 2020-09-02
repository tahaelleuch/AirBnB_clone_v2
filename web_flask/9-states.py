#!/usr/bin/python3
"""flask"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def tr_down(exception):
    """close session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_byid(id=None):
    """print choosed states"""
    all_states = storage.all("State")
    if id is None:
        return render_template('9-states.html', all_states=all_states)
    else:
        for state in storage.all("State").values():
            if state.id == id:
                id_state = state
                return render_template("9-states.html", id_state=id_state)
    return render_template("9-states.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
