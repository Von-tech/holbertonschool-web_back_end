#!/usr/bin/env python3
""" Task 5:  Encrypting passwords taken from 0x02-Personal Data project """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """
    password = password.encode('utf-8')
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register user in database """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hash_pw = _hash_password(password)
            user = self._db.add_user(email, hash_pw)
            return user
        else:
            raise ValueError("User {} already exists".format(email))
