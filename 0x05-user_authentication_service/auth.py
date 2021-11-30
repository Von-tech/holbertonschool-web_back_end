#!/usr/bin/env python3
""" Task 5:  Encrypting passwords taken from 0x02-Personal Data project """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """
    password = password.encode('utf-8')
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash
