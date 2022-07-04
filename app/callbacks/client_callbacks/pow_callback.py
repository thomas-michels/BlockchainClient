"""
    Module for Validate Chain
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventClientSchema
from app.configs import get_logger, get_environment
from app.worker.producer import KombuProducer
from app.utils import generate_event, generate_hash
from random import randint

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
            _env.POW_ACTIVE = True
            hash_nonce = message.payload["nonce"]
            hash_atual = ""
            while _env.POW_ACTIVE and hash_nonce != hash_atual:
                nonce = randint(100, 900)
                hash_atual = generate_hash(nonce)

            _logger.info("POW completed")
            # if hash_nonce == hash_atual:
            payload = {
                "client_name": message.sended_to,
                "nonce_hashed": hash_atual,
                "nonce": nonce,
                "data": message.payload["data"]
            }
            producer = KombuProducer()
            event = generate_event(_env.ELECTION_CHANNEL, payload)
            producer.send_messages(event)

            return True

        except Exception as error:
            _logger.error(f"Error on POWCallback: {error}")
            return False
