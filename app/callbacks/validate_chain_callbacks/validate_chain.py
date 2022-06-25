"""
    Module for Validate Chain
"""
from typing import List
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventSchema
from app.configs import get_logger
from app.utils import generate_hash
from app.exceptions import InvalidChain

_logger = get_logger(name=__name__)


class ValidateChain(CallbackInterface):
    """
    Validate chain class
    """

    def handle(self, message: EventSchema) -> bool:
        _logger.info(f"Starting Validate Blockchain")
        try:
            blocks: List[dict] = message.payload["data"]
            for i in range(len(blocks) - 1):
                current = blocks[i]
                next = blocks[i + 1]
                if current["hash"] != next["previous_hash"] or self.__validate_current_hash(current):
                    raise InvalidChain()

            _logger.info("Blockchain validated with success")
            return True

        except Exception as error:
            _logger.error(f"Error on proccess Validate Chain: {error}")
            return False

    def __validate_current_hash(self, current: dict) -> bool:
        """
        Method for validate current hash

        :param current: dict
        :return: bool
        """
        hash_dict = current["hash"]
        current.pop("hash")
        current_hash = generate_hash(current.__str__())
        return hash_dict != current_hash
