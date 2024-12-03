from untils.api import GoogleMapsApi


class TestGoogleMapsApi:

    # тестирование методов api
    def test_methods_api(self):
        print("\nМетод POST")
        new_place = GoogleMapsApi.create_new_place()
        place_id = new_place.json()["place_id"]

        print("\nМетод GET, после метода POST")
        GoogleMapsApi.get_place(place_id)

        print("\nМетод PUT")
        GoogleMapsApi.put_place(place_id)

        print("\nМетод GET, после метода PUT")
        GoogleMapsApi.get_place(place_id)

        print("\nМетод DELETE")
        GoogleMapsApi.delete_place(place_id)

        print("\nМетод GET, после метода DELETE")
        GoogleMapsApi.get_place(place_id)
