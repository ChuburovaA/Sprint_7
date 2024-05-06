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

    @allure.title("Проверка введения несуществующего логина курьера")
    def test_nonexistent_login_courier(self):
        payload = {
            'login': Helper.generate_random_string(10),
            'password': Helper.generate_random_string(10)
        }
        response = requests.post(URL.url_login_courier, data=payload)

        assert response.status_code == 404 and response.json()['message'] == TextMessage.account_not_found