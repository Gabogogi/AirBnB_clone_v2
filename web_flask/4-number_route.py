#!/usr/bin/python3
'''
starts a flask web app
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    displays feedback to / route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    displays feedback to /hbnb
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''displays C followed by value of text'''
    to_replace = '_'
    replaced_by = ' '
    new_text = text.replace(to_replace, replaced_by)
    return f'C {new_text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_is_cool(text="is cool"):
    '''displays Python followed by value of text'''
    to_replace = '_'
    replaced_by = ' '
    new_text = text.replace(to_replace, replaced_by)
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_display(n):
    '''checks if no in route is integer'''
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
