from app.worker.producer import KombuProducer
from app.utils import generate_event

KombuProducer.send_messages(
    generate_event("aa", "VALIDATE", {"data": ["teste"], "nonce": 1234})
)
