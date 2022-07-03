"""
This module start connection with queues
"""

from app.worker.consumer import RegisterQueues
from app.configs import get_logger
from app.worker import KombuWorker
from app.worker.utils import start_connection_bus
from app.utils import generate_client
from app.callbacks import SendRegistrationCallback

_logger = get_logger(name=__name__)


class Application:
    """This class start connection and worker"""

    def __init__(self) -> None:
        _logger.info("Creating Connection...")
        # account_number = int(input("Insira o número da sua conta: "))
        account_number = 315007
        client = generate_client(account_number)

        register_queue = RegisterQueues(client_name=client.name)
        queues = register_queue.register()

        SendRegistrationCallback().handle(client)

        _logger.info(f"Tokens will be sended for account with number {account_number}")

        self.start_consuming(queues)

    def start_consuming(self, queues):
        _logger.info("Start consuming...")
        try:
            with start_connection_bus() as conn:
                worker = KombuWorker(conn, queues)
                worker.run()

        except KeyboardInterrupt:
            _logger.info("Exiting...")
            quit()
