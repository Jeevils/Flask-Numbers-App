from flask import Flask, Response, jsonify
import json
from flask import json
import sys
from flask import jsonify

app = Flask(__name__)

@app.route('/number/<input>', methods=['GET', 'POST'])
def fizzbuzz(input):
    fizzbuzz = ''
    try:
        input = int(float(input))
    except ValueError:
        return "ValueError: please enter a number"
    if input % 3 == 0 and input % 5 == 0:
        fizzbuzz = 'fizzbuzz'
    elif input % 3 == 0:
        fizzbuzz = 'fizz'
    elif input % 5 == 0:
        fizzbuzz = 'buzz'
    else:
        return input
    return fizzbuzz