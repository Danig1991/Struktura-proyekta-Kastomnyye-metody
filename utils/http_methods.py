import requests

from configurations.path_key import HEADERS, COOKIE
from utils.logger import Logger


class HttpMethods:
    # метод Get
    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(
            url=url,
            headers=HEADERS,
            cookies=COOKIE
        )
        Logger.add_response(result)
        return result

    # метод Post
    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(
            url=url,
            json=body,
            headers=HEADERS,
            cookies=COOKIE
        )
        Logger.add_response(result)
        return result

    # метод Put
    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(
            url=url,
            json=body,
            headers=HEADERS,
            cookies=COOKIE
        )
        Logger.add_response(result)
        return result

    # метод Delete
    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(
            url=url,
            json=body,
            headers=HEADERS,
            cookies=COOKIE
        )
        Logger.add_response(result)
        return result
