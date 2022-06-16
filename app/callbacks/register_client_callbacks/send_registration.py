"""
    Module for send registration callback
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.client import SimpleClientSchema
from app.worker.producer import KombuProducer
from app.utils import generate_event
from app.configs import get_logger, get_environment

_env = get_environment()
_logger = get_logger(name=__name__)


class SendRegistrationCallback(CallbackInterface):
    """
    SendRegistrationCallback class
    """

    def handle(self, message: SimpleClientSchema) -> bool:
        event = generate_event(message.client_id, _env.REGISTER_CHANNEL, message.dict())
        KombuProducer.send_messages(event)
        _logger.info(f"Client Registred with name {message.name}")
        return True
