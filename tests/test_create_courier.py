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

    @allure.title("Проверка создания курьера уже с существующими данными")
    def test_create_courier_with_existing_data(self, create_new_courier, login_and_delete_courier):
        payload = create_new_courier
        response = requests.post(URL.url_create_courier, data=payload)

        assert response.status_code == 409 and response.json()["message"] == TextMessage.used_login