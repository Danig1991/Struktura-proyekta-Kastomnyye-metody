from configurations.configurations import BASE_URL, POST_RESOURCE, KEY, body_to_creating_location
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
