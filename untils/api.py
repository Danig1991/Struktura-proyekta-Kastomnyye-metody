from configurations.configurations import (
    BASE_URL,
    POST_RESOURCE,
    GET_RESOURCE,
    KEY,
    body_to_creating_location
)
from untils.http_methods import HttpMethods


class GoogleMapsApi:
    # создание новой локации
    @staticmethod
    def create_new_place():
        post_url = BASE_URL + POST_RESOURCE + KEY
        print(f"URL для создания локации:\n{post_url}")

        result_post = HttpMethods.post(url=post_url, body=body_to_creating_location())
        print(f"Ответ сервера:\n{result_post.json()}")
        return result_post

    # получить локацию
    @staticmethod
    def get_place(place_id):
        get_url = BASE_URL + GET_RESOURCE + KEY + "&place_id=" + place_id
        print(f"URL для получения локации:\n{get_url}")

        result_get = HttpMethods.get(url=get_url)
        print(f"Ответ сервера:\n{result_get.json()}")
        return result_get
