#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from typing import Dict
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = os.getenv('AUTH_TYPE')
if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
excluded_paths = ['/api/v1/status/',
                  '/api/v1/unauthorized/', '/api/v1/forbidden/']


@app.before_request
def before_request() -> Dict:
    """ Filtering each request with handler """
    if auth and auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None:
            abort(401)
        elif auth.current_user(request) is None:
            abort(403)
        request.current_user = auth.current_user(request)


@app.errorhandler(401)
def unauthorized_req(error) -> str:
    """ HTTP status code for a request unauthorized """
    return (jsonify({"error": "Unauthorized"}), 401)


@app.errorhandler(403)
def forbidden_req(error) -> str:
    """  HTTP status code for a req where user cannot access a resource """
    return (jsonify({"error": "Forbidden"}), 403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
