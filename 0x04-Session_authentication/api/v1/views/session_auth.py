#!/usr/bin/env python3
""" Task 7: New view for Session Authentication """
from flask.helpers import make_response
from api.v1.views import app_views
from flask import abort, jsonify, request, session
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ New Flask view that handles all routes for the authentication """
    from api.v1.app import auth
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    if user_email is None or user_email == "":
        return jsonify({"error": "email missing"}), 400
    elif user_password is None or user_password == "":
        return jsonify({"error": "password missing"}), 400
    user_list = User.search({"email": user_email})
    if len(user_list) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_list[0]
    if not user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401
    session_id = auth.create_session(user.id)
    cookie_name = os.getenv("SESSION_NAME")
    response = make_response(user.to_json())
    response.set_cookie(cookie_name, session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def auth_session_logout():
    """ Updating file by adding new route """
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if not destroy_session:
        abort(404)
    return jsonify({}), 200
