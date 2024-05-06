class URL:

    url_login_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    url_create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    url_create_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    url_get_order_list = 'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId='
    url_accept_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept'
    url_get_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/track'

class TextMessage:
    account_not_found = 'Учетная запись не найдена'
    no_login_information = "Недостаточно данных для входа"
    no_information_to_account = 'Недостаточно данных для создания учетной записи'
    used_login = 'Этот логин уже используется. Попробуйте другой.'
    successful_registration = '{"ok":true}'

class OrderData:
    order_data = {
        "firstName": "Екатерина II",
        "lastName": "Романова",
        "address": "Санкт-Петербург, Дворцовая набережная 38",
        "metroStation": 10,
        "phone": "+7 000 111 22 33",
        "rentTime": 3,
        "deliveryDate": "2024-06-28",
        "comment": "Попрошу-с не опаздывать!",
        "color": [
            "BLACK"
        ]
    }

    color_list = ['BLACK', 'GREY', 'BLACK, GREY', '']