import requests

from configurations.path_key import HEADERS, COOKIE


class HttpMethods:
    # метод Get
    @staticmethod
    def get(url):
        result = requests.get(
            url=url,
            headers=HEADERS,
            cookies=COOKIE
        )
        return result

    # метод Post
    @staticmethod
    def post(url, body):
        result = requests.post(
            url=url,
            json=body,
            headers=HEADERS,
            cookies=COOKIE
        )
        return result

    # метод Put
    @staticmethod
    def put(url, body):
        result = requests.put(
            url=url,
            json=body,
            headers=HEADERS,
            cookies=COOKIE
        )
        return result

    # метод Delete
    @staticmethod
    def delete(url, body):
        result = requests.delete(
            url=url,
            json=body,
            headers=HEADERS,
            cookies=COOKIE
        )
        return result
