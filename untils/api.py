from configurations.body import (
    body_to_creating_location,
    body_for_location_update,
    body_to_remove_location
)
from configurations.path_key import (
    BASE_URL,
    POST_RESOURCE,
    KEY,
    GET_RESOURCE,
    PUT_RESOURCE,
    DELETE_RESOURCE
)
from untils.http_methods import HttpMethods


class GoogleMapsApi:
    # создание новой локации
    @staticmethod
    def create_new_place():
        post_url = BASE_URL + POST_RESOURCE + "?key=" + KEY
        print(f"URL для создания локации:\n{post_url}")

        result_post = HttpMethods.post(
            url=post_url,
            body=body_to_creating_location()
        )
        print(f"Ответ сервера:\n{result_post.json()}")
        return result_post

    # получить локацию
    @staticmethod
    def get_place(place_id):
        get_url = BASE_URL + GET_RESOURCE + "?key=" + KEY + "&place_id=" + place_id
        print(f"URL для получения локации:\n{get_url}")

        result_get = HttpMethods.get(url=get_url)
        print(f"Ответ сервера:\n{result_get.json()}")
        return result_get

    # обновить локацию
    @staticmethod
    def put_place(place_id):
        put_url = BASE_URL + PUT_RESOURCE + "?key=" + KEY
        print(f"URL для обновления локации:\n{put_url}")

        result_put = HttpMethods.put(
            url=put_url,
            body=body_for_location_update(place_id=place_id, key=KEY)
        )
        print(f"Ответ сервера:\n{result_put.json()}")
        return result_put

    # удалить локацию
    @staticmethod
    def delete_place(place_id):
        delete_url = BASE_URL + DELETE_RESOURCE + "?key=" + KEY
        print(f"URL для удаления локации:\n{delete_url}")

        result_delete = HttpMethods.delete(
            url=delete_url,
            body=body_to_remove_location(place_id=place_id)
        )
        print(f"Ответ сервера:\n{result_delete.json()}")
        return result_delete
