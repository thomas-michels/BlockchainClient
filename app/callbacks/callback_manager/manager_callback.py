"""
    Module for Validate Chain
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventClientSchema
from app.callbacks.validate_chain_callbacks import ValidateChain
from app.callbacks.client_callbacks import POWCallback
from app.configs import get_logger, get_environment

_logger = get_logger(name=__name__)
_env = get_environment()


class ManagerCallback(CallbackInterface):
    """
    Validate chain class
    """

    def handle(self, message: EventClientSchema) -> bool:
        try:
            if message.function == _env.VALIDATE_FUNCTION:
                return ValidateChain().handle(message)

            elif message.function == _env.POW_FUNCTION:
                return POWCallback().handle(message)

            return False

        except Exception as error:
            _logger.error(f"Error on ManagerCallback: {error}")
            return False
