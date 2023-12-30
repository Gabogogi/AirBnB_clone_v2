#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
#from models import storage
#from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    '''List all states '''
    states = list(storage.all(State).values())
    # Sort states by name alphabetically in ascending order
    states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
