#!/usr/bin/env python3
""" Basic Auth Class """
from api.v1.auth.auth import Auth
from models.user import User
import base64
from models.base import DATA
from typing import TypeVar


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
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            return base64.b64decode(base64_authorization_header,
                                    None, False).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Method that returns email/password from Base64 decoded value """
        special_colon = ':'
        if decoded_base64_authorization_header is None:
            return None, None
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None
        if special_colon not in decoded_base64_authorization_header:
            return None, None
        else:
            values = decoded_base64_authorization_header.split(':')
            return values

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Method that returns User instance based on his email/password """
        if user_email is None or not isinstance(user_email, str):
            return None
        elif user_pwd is None or not isinstance(user_pwd, str):
            return None
        elif not DATA.get('User'):
            return None
        Search_users = User.search({'email': user_email})
        for user in Search_users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that overloads Auth & retrieves User instance for a req """
        auth_header = super().authorization_header(request)
        extract64 = self.extract_base64_authorization_header(auth_header)
        decode64 = self.decode_base64_authorization_header(extract64)
        email, pas = self.extract_user_credentials(decode64)
        user_obj = self.user_object_from_credentials(email, pas)
        return user_obj
