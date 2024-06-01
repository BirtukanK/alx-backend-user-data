#!/usr/bin/env python3
"""
implement a hash_password function
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ takes password and hashs it"""
    to_hash = b'password'
    hashed = bcrypt.hashpw(to_hash, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks if hashed one is vaid for given password"""
    if bcrypt.checkpw(b'password', hashed_password):
        return True
    else:
        return False
