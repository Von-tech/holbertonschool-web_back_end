#!/usr/bin/env python3
""" Task 3: Auth class """
from typing import List, TypeVar
from flask import request


class Auth:
    """ This class is used to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check for excluded paths """

        backslash = '/'

        if excluded_paths is None:
            return True

        if excluded_paths is not len(excluded_paths):
            return True

        if path is None:
            return True

        if path in excluded_paths:
            return False

        if path + backslash in excluded_paths:
            return False

        return True


def authorization_header(self, request=None) -> str:
    """ Public method that return None - request """
    if request is None
    return None
    if request.headers.get('Authorization') is None:
        return None
    return request.headers.get('Authorization')


def current_user(self, request=None) -> TypeVar('User'):
    """ Public method that return None - request """
    return None
