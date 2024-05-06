import requests
import pytest

from data import URL
from helpers import Helper

@pytest.fixture
def create_new_courier():
    login = Helper.generate_random_string(10)
    password = Helper.generate_random_string(10)
    first_name = Helper.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload