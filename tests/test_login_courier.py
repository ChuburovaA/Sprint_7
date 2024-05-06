import pytest
import allure
import requests

from data import URL, TextMessage
from helpers import Helper
from conftest import create_new_courier, login_and_delete_courier, register_new_courier

@allure.story("Проверки на логин курьера")
class TestLoginCourier:

    @allure.title("Проверка наличия id при успешном логине курьера")
    def test_successful_login_courier(self, login_and_delete_courier):
        response = login_and_delete_courier
        response_body = response.json()

        assert response.status_code == 200 and 'id' in response_body.keys()