#!/usr/bin/env python3
""" Task 6: Setup basic Flask app """
from flask import abort, Flask, jsonify, request, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def begin():
    """ GET route that uses flask.jsonify to return a JSON payload """
    return jsonify({'message': 'Bienvenue'})


@app.route("/users", methods=["POST"])
def users():
    """ Method implements the end-point to register a user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if AUTH.register_user(email, password):
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """ Method to log in user """
    email = request.form.get("email")
    password = request.form.get("password")
    valid_user = AUTH.valid_login(email=email, password=password)
    if not valid_user:
        abort(401)
    session_id = AUTH.create_session(email=email)
    response = jsonify({"email": email, "message": "logged in "})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
