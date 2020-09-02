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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text="is cool"):
    """python text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numhtml(n):
    """number on html"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
