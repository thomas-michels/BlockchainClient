"""
    Module for Client generator
"""
from app.utils.name_generator import get_fake_name
from app.utils.uuid_generator import generate_uuid
from app.crud.client import SimpleClientSchema


def generate_client() -> SimpleClientSchema:
    """
    Function to generate a new client

    :return: SimpleClientSchema
    """
    payload = {
        "client_id": generate_uuid(),
        "name": get_fake_name()
    }
    return SimpleClientSchema(**payload)
