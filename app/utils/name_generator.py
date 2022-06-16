"""
    Module for name generator
"""

from faker import Faker

def get_fake_name() -> str:
    faker = Faker()
    return faker.name()
