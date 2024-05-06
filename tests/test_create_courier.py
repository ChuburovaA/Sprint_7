import pytest
import allure
import requests

from data import URL, TextMessage
from helpers import Helper
from conftest import create_new_courier, register_new_courier, login_and_delete_courier

@allure.story("Проверки на создание курьера")
class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    def test_registration_courier_successful(self, register_new_courier, login_and_delete_courier):
        response = register_new_courier

        assert response.status_code == 201 and response.text == TextMessage.successful_registration