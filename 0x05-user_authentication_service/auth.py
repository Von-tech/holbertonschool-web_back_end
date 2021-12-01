#!/usr/bin/env python3
""" Task 5:  Encrypting passwords taken from 0x02-Personal Data project """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


def _hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """
    password = password.encode('utf-8')
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash


def _generate_uuid() -> str:
    """ Method that returns a str repr of a new UUID """
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """ Method that takes email str arg & returns the session ID as str """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Method takes a single session_id string arg & returns the user """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Method takes a single user_id integer arg and returns None """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Method takes an email string argument and returns a string """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(found_user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method takes reset_token str arg & pw str arg & returns None """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password)
            self._db.update_user(user.id, reset_token=None)
        except NoResultFound:
            raise ValueError
