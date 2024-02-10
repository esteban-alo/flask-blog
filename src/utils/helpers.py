"""
Helpers functions
"""

import hashlib
from uuid import uuid4


def generate_salt() -> str:
    """
    Generates a character lowercase hexadecimal string
    :return: alphanumeric string
    """
    return uuid4().hex


def hash_password(password: str, salt: str) -> str:
    """
    Creates SHA-512 hash string from a password string and salt
    :param password: string is going to be hashed
    :param salt: hexadecimal string
    :return: hashed password string
    """
    fmt_password = bytes(password + salt, "utf-8")
    hashed_password = hashlib.sha512(fmt_password).hexdigest()

    return hashed_password
