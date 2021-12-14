#!/usr/bin/env python3
""" Task 0: Writing strings to Redis """
import redis
from uuid import uuid4
from typing import Union


class Cache():
    """ New class stores an instance of the Redis client as a private var """
    def __init__(self):
        """ Storing instance """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method generates a random key and stores the input data in Redis """
        rand_key = str(uuid4())
        self._redis.set(rand_key, data)
        return rand_key


    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Method will get the value of key if it exists """
        if fn is not None:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)


    def get_str(self, key: str) -> str:
        """  Parametrize Cache.get with the correct conversion function.
        Takes a bytes string and return to a str.
        """
        return self.get(key, str)


    def get_int(self, key: str) -> int:
        """  Parametrize Cache.get with the correct conversion function.
        Takes a bytes string and return to a int.
        """
        return self.get(key, int)
