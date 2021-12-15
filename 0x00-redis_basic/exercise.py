#!/usr/bin/env python3
""" Task 0: Writing strings to Redis """
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ System counts how many times methods of the Cache class are called """
    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """ Here is our wrapper func for count_calls """
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Store the history of inputs and outputs """
    input_list_key = method.__qualname__ + ":inputs"
    output_list_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """ Here is our wrapper for call_history """
        self._redis.rpush(input_list_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list_key, output)
        return output
    return wrapper


def replay(method: Callable) -> Callable:
    """ Method to display the history of calls of a particular function.
    Tip: use lrange and zip to loop over inputs and outputs in history
    When the server returns bytes, it will be converted into a str
    """
    r_var = method.__self__._redis
    self = method.__qualname__

    aux = r_var.get(self).decode('utf-8')
    inputs = r_var.lrange(method.__qualname__ + ':inputs', 0, -1)
    outputs = r_var.lrange(method.__qualname__ + ':outputs', 0, -1)
    print("{} was called {} times:".format(method.__qualname__, aux))
    for input, output in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(self, input.decode("utf-8"),
                                     output.decode("utf-8")))


class Cache():
    """ New class stores an instance of the Redis client as a private var """
    def __init__(self):
        """ Storing instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method generates a rand key & stores the input data in Redis """
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
