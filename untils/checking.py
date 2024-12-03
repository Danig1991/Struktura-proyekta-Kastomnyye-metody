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

    # проверка содержания слова в поле
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check_info = response.json()[field_name]
        if search_word in check_info:
            print(f"Слово \"{search_word}\" содержится в поле \"{field_name}\"")
        else:
            print(f"Слово \"{search_word}\" не содержится в поле \"{field_name}\"")
