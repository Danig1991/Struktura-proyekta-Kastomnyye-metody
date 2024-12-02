from untils.api import GoogleMapsApi


class TestGoogleMapsApi:
    place_id = ""

    @classmethod
    def test_create_new_place(cls):
        print("\nМетод POST")
        new_place = GoogleMapsApi.create_new_place()
        cls.place_id = new_place.json()["place_id"]

    @classmethod
    def test_get_place(cls, method="POST"):
        print(f"\nМетод GET, после {method}")
        print(f"Запрос по place_id = {cls.place_id}")
        GoogleMapsApi.get_place(cls.place_id)

    @classmethod
    def test_put_place(cls):
        print("\nМетод PUT")
        GoogleMapsApi.put_place(cls.place_id)
        cls.test_get_place(method="PUT")

    @classmethod
    def test_delete_place(cls):
        print("\nМетод DELETE")
        GoogleMapsApi.delete_place(cls.place_id)
        cls.test_get_place(method="DELETE")
