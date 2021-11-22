#!/usr/bin/env python3
""" Task 6: Basic Auth """
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ New class that inherits from Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """ Method that returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        if authorization_header.startswith('Basic ') is False:
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ Method that returns the decoded value of a Base64 string """
        """ if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        """
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
