#!/usr/bin/env python3
""" Task 5:  Encrypting passwords taken from 0x02-Personal Data project """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Method that checks user password """
        try:
            user = self._db.find_user_by(email=email)
            pw = password.encode('UTF-8')
            if bcrypt.checkpw(pw, user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """ Method that returns a str repr of a new UUID """
        new = str(uuid4())
        return new
