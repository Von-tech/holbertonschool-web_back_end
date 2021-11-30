#!/usr/bin/env python3
""" Task 6: Setup basic Flask app """
from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def begin():
    """ GET route that uses flask.jsonify to return a JSON payload """
    return jsonify({'message': 'Bienvenue'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
