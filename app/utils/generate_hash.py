"""
    Module for generate hash
"""
from hashlib import sha256


def generate_hash(payload_str: str) -> str:
    """
    Function to generate hash

    :param block: BlockSchema
    :return: str
    """
    sha256_function = sha256()
    sha256_function.update(bytes(payload_str, encoding="utf-8"))
    return sha256_function.hexdigest()
