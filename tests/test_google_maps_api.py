from configurations.expected_value import (
    MESSAGE,
    STATUS,
    LOCATION_VALUES,
    VALUES_IN_RESPONSE_POST
)
from untils.api import GoogleMapsApi
from untils.checking import Checking


class TestGoogleMapsApi:

    # тестирование методов api
    @staticmethod
    def test_methods_api():
        print("\nМетод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json()["place_id"]

        Checking.check_status_code(response=result_post, status_code=200)
        Checking.check_json_token(response=result_post, expected_value=VALUES_IN_RESPONSE_POST)
        Checking.check_json_search_word_in_value(response=result_post, field_name="status", search_word="OK")

        tests = [
            ("\nМетод GET, после метода POST", GoogleMapsApi.get_place, place_id, 200, LOCATION_VALUES,
             "address", "side layout"),
            ("\nМетод PUT", GoogleMapsApi.put_place, place_id, 200, MESSAGE, "msg", "successfully"),
            ("\nМетод GET, после метода PUT", GoogleMapsApi.get_place, place_id, 200, LOCATION_VALUES,
             "address", "Lenina street"),
            ("\nМетод DELETE", GoogleMapsApi.delete_place, place_id, 200, STATUS, "status", "OK"),
            ("\nМетод GET, после метода DELETE", GoogleMapsApi.get_place, place_id, 404, MESSAGE, "msg", "failed")
        ]

        for test_name, method, *args, status_code, expected_value, field_name, search_word in tests:
            print(test_name)

            result = method(*args)

            Checking.check_status_code(result, status_code)
            Checking.check_json_token(result, expected_value)
            Checking.check_json_search_word_in_value(result, field_name, search_word)

        print("\nТестирование создания, изменения и "
              "удаления новой локации прошло успешно.")
