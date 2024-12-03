import json

from requests import Response


class Checking:
    # проверка статус-кода
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Успешно! Статус код = {str(response.status_code)}")
        else:
            print(f"Ошибка! Статус код = {str(response.status_code)}")

    # проверка присутствия обязательных полей
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все обязательные поля присутствуют!")
