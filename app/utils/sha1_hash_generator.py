"""
    Module for SHA1 hash generator
"""
from hashlib import sha1


def generate_hash(number: int) -> str:
    """
    Function to generate hash SHA1

    :param number: int
    :return: str
    """
    hash = sha1(bytes(number))
    return hash.hexdigest()
