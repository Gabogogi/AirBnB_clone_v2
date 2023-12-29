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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
