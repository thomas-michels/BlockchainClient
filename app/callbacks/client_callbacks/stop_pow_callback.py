"""
    Module for Validate Chain
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventClientSchema
from app.configs import get_logger, get_environment

_logger = get_logger(name=__name__)
_env = get_environment()


class StopPOWCallback(CallbackInterface):
    """
    StopPOWCallback
    """

    def handle(self, message: EventClientSchema) -> bool:
        try:
            _logger.info("Stopping POW")
            _logger.info(f"Winner: {message.payload['winner']}")
            _env.POW_ACTIVE = False
            return True

        except Exception as error:
            _logger.error(f"Error on StopPOWCallback: {error}")
            return False
