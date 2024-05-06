import pytest
import allure
import requests
import json

from data import URL, TextMessage, OrderData
from conftest import create_new_courier, login_and_delete_courier, register_new_courier

@allure.story("Проверки на создание заказа и получение списка")
class TestOrder:

    @allure.title("Проверка получения успешного заказа при выборе цветов самоката из списка")
    @pytest.mark.parametrize('color', OrderData.color_list)
    def test_add_color_in_order(self, color):
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(OrderData.order_data)
        response = requests.post(URL.url_create_order, data=payload)
        response_body = response.json()

        assert response.status_code == 201 and 'track' in response_body.keys()

    @allure.title("Проверка получения списка заказов курьера")
    def test_order_list_from_courier(self, login_and_delete_courier):
        login = login_and_delete_courier
        create_order = requests.post(URL.url_create_order, data=json.dumps(OrderData.order_data))
        get_order = requests.get(f"{URL.url_get_order}?t={create_order.json()['track']}")

        requests.put(f"{URL.url_accept_order}/{get_order.json()['order']['id']}?courierId={login.json()['id']}")
        get_order_list = requests.get(f"{URL.url_get_order_list}{login.json()['id']}")

        assert get_order_list.json()['orders'][0]['id'] == get_order.json()['order']['id']