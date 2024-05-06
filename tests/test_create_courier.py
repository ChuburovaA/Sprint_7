import pytest
import allure
import requests

from data import URL, TextMessage
from helpers import Helper
from conftest import create_new_courier, register_new_courier, login_and_delete_courier

class TestCreateCourier: