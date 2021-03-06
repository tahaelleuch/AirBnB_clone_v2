#!/usr/bin/python3
"""flask new"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """print text"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
