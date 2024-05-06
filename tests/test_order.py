import pytest
import allure
import requests
import json

from data import URL, TextMessage, OrderData
from conftest import create_new_courier, login_and_delete_courier, register_new_courier

@allure.story("Проверки на создание заказа и получение списка")
class TestOrder: