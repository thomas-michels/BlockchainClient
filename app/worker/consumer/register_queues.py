"""
    Module for register queues
"""
from app.worker.consumer.manager import QueueManager
from app.configs import get_logger, get_environment
from app.callbacks import ManagerCallback

_logger = get_logger(name=__name__)
_env = get_environment()


class RegisterQueues:
    """
    RegisterQueues class
    """

    def __init__(self, client_name: str = "") -> None:
        self.__client_queue = client_name

    def register(self) -> QueueManager:
        _logger.info("Starting QueueManager")
        queue_manager = QueueManager()

        if self.__client_queue:
            queue_manager.register_callback(self.__client_queue, ManagerCallback().handle)

        _logger.info("All queues started")

        return queue_manager
