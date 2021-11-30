#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method that creates and adds new user to the database """
        create_new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(create_new_user)
        self._session.commit()
        return create_new_user

    def find_user_by(self, **kwargs) -> User:
        """ Method takes in arbitrary kw args and returns first row """
        first_row = self._session.query(User).filter_by(**kwargs)
        return first_row.one()

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """ Method takes a required user_id int and arbitrary kw args """
        user_update = self.find_user_by(id=user_id)
        for key in kwargs:
            try:
                setattr(user_update, key, kwargs[key])
            except:
                raise ValueError
        self._session.commit()
