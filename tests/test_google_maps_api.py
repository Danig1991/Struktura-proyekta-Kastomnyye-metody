from untils.api import GoogleMapsApi


class TestGoogleMapsApi:

    def test_create_new_place(self):
        print("\nМетод POST")
        GoogleMapsApi.create_new_place()
