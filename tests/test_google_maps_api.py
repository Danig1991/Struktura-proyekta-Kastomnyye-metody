from untils.api import GoogleMapsApi
from untils.checking import Checking


class TestGoogleMapsApi:

    # тестирование методов api
    @staticmethod
    def test_methods_api():
        print("\nМетод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json()["place_id"]
        Checking.check_status_code(result_post, 200)

        print("\nМетод GET, после метода POST")
        result_get = GoogleMapsApi.get_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("\nМетод PUT")
        result_put = GoogleMapsApi.put_place(place_id)
        Checking.check_status_code(result_put, 200)

        print("\nМетод GET, после метода PUT")
        result_get = GoogleMapsApi.get_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("\nМетод DELETE")
        result_delete = GoogleMapsApi.delete_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("\nМетод GET, после метода DELETE")
        result_get = GoogleMapsApi.get_place(place_id)
        Checking.check_status_code(result_get, 404)
