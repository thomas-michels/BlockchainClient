"""
    Module for Validate Chain
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventClientSchema
from app.configs import get_logger, get_environment

_logger = get_logger(name=__name__)
_env = get_environment()


class POWCallback(CallbackInterface):
    """
    POWCallback
    """

    def handle(self, message: EventClientSchema) -> bool:
        try:
            _logger.info("Starting POW")
            _logger.info(f"message: {message}")
            _logger.info("POW completed")
            return True

        except Exception as error:
            _logger.error(f"Error on POWCallback: {error}")
            return False
