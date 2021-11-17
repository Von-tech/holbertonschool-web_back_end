#!/usr/bin/env python3
""" Task 5:  Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """
    password = password.encode('utf-8')
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Use bcrypt to validate that password matches the hashed password """
    password = password.encode('utf-8')
    if bcrypt.checkpw(password, hashed_password):
        return True
    else:
        return False
