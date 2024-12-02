from untils.api import GoogleMapsApi


class TestGoogleMapsApi:
    place_id = ""

    @classmethod
    def test_create_new_place(cls):
        print("\nМетод POST")
        new_place = GoogleMapsApi.create_new_place()
        cls.place_id = new_place.json()["place_id"]

    @classmethod
    def test_get_place(cls):
        print("\nМетод GET")
        print(f"Запрос по place_id = {cls.place_id}")
        GoogleMapsApi.get_place(cls.place_id)
