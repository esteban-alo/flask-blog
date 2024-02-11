"""
Helpers functions tests cases
"""

from src.utils.helpers import generate_salt, hash_password

SALT_STRING = generate_salt()


def test_generate_salt_length():
    """
    Test salt string length
    """
    assert len(SALT_STRING) >= 32


def test_hash_password():
    """
    Test hash_password hashes string
    """
    hashed_password = hash_password(password="some_string", salt=SALT_STRING)
    assert len(hashed_password) >= 32
