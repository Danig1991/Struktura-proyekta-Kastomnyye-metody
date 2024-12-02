import requests


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(
            url=url,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(
            url=url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(
            url=url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(
            url=url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result
