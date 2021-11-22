#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views

""" By calling abort(...) the error handler for ... will be executed """
""" Below are endpoints used for testing the newly added error handlers """

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ Endpoint that raises a 401 error by using abort """
    abort(401)

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
    """ Endpoint that raises a 401 error by using abort """
    abort(403)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
