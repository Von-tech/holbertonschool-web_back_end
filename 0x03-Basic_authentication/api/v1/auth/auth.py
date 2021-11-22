#!/usr/bin/env python3
""" Task 3: Auth class """
from typing import List, TypeVar
from flask import request


class Auth:
    """ This class is used to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check for excluded paths """
        backslash = '/'

        if path is None or excluded_paths is None:
            return True
        if not excluded_paths:
            return True
        if path[-1] != backslash:
            path += backslash
        if path not in excluded_paths:
            return True
        else:
            return False


def authorization_header(self, request=None) -> str:
    """ Public method that return None - request """
    if request is None or request.headers.get('Authorization') is None:
        return None
    return request.headers.get('Authorization')


def current_user(self, request=None) -> TypeVar('User'):
    """ Public method that return None - request """
    return None
