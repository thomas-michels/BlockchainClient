"""
    Module for Validate Chain
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventClientSchema
from app.configs import get_logger, get_environment
from app.worker.producer import KombuProducer
from app.utils import generate_event

_logger = get_logger(name=__name__)
_env = get_environment()


class NewBlockCallback(CallbackInterface):
    """
    NewBlockCallback
    """

    def handle(self, message: EventClientSchema) -> bool:
        try:
            producer = KombuProducer()
            event = generate_event(_env.BLOCK_CHANNEL, message.payload)
            producer.send_messages(event)

            return True

        except Exception as error:
            _logger.error(f"Error on NewBlockCallback: {error}")
            return False
