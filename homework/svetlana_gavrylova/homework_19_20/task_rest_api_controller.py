import requests
import curlify

BASE_URI = 'https://api.restful-api.dev'


def get_all_list():
    url = f'{BASE_URI}/objects'
    r = requests.get(url)
    curl = curlify.to_curl(r.request)

    return r, curl


def get_list_by_ids(*args):
    url = f'{BASE_URI}/objects?'
    for i in args:
        url += f'id={i}&'
    r = requests.get(url)
    curl = curlify.to_curl(r.request)

    return r, curl


def get_single_object_by_id(object_id):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.get(url)
    curl = curlify.to_curl(r.request)

    return r, curl


def add_object(name, year, price, cpu_model, hard_disk_size):
    url = f'{BASE_URI}/objects'
    payload = {
        "name": name,
        "data": {
            "year": year,
            "price": price,
            "CPU model": cpu_model,
            "Hard disk size": hard_disk_size
        }
    }

    r = requests.post(url, json=payload)
    curl = curlify.to_curl(r.request)

    return r, curl


def update_object(object_id, payload):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.put(url, json=payload)
    curl = curlify.to_curl(r.request)

    return r, curl


def update_partial_object(object_id, partial_payload):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.patch(url, json=partial_payload)
    curl = curlify.to_curl(r.request)

    return r, curl


def delete_object(object_id):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.delete(url)
    curl = curlify.to_curl(r.request)

    return r, curl
