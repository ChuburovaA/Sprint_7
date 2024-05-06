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