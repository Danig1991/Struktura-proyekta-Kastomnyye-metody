# базовый URL
BASE_URL = "https://rahulshettyacademy.com"

# путь до ресурса с методом
POST_RESOURCE = "/maps/api/place/add/json"
GET_RESOURCE = "/maps/api/place/get/json"
PUT_RESOURCE = "/maps/api/place/update/json"
DELETE_RESOURCE = "/maps/api/place/delete/json"

# ключ
KEY = "qaclick123"

# хедерс/куки
HEADERS = {'Content-Type': 'application/json'}
COOKIE = ""


# тело для создания локации
def body_to_creating_location():
    return {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }


# тело для обновления локации
def body_for_location_update(place_id, key):
    return {
        "place_id": place_id,
        "address": "100 Lenina street, RU",
        "key": key
    }


# тело для удаления локации
def body_to_remove_location(place_id):
    return {
        "place_id": place_id
    }
