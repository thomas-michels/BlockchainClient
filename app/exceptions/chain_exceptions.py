"""
    Module for chain exceptions
"""

class InvalidChain(Exception):
    """
    Raised when blockchain is invalid
    """

    def __init__(self, *args: object) -> None:
        message = "Invalid blockchain"
        super().__init__(*args, message)
