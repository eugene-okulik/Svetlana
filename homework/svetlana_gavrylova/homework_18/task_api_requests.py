import requests
import curlify

BASE_URI = 'https://api.restful-api.dev'


def get_all_list():
    url = f'{BASE_URI}/objects'
    r = requests.get(url)
    curl = curlify.to_curl(r.request)

    assert r.status_code == 200, f'Status code is incorrect: {r.status_code}\n{curl}'
    assert isinstance(r.json(), list), f'List is not returned\n{curl}'

    return r.json(), curl


def get_list_by_ids(*args):
    url = f'{BASE_URI}/objects?'
    for i in args:
        url += f'id={i}&'
    r = requests.get(url)
    curl = curlify.to_curl(r.request)

    assert r.status_code == 200, f'Status code is incorrect: {r.status_code}\n{curl}'
    assert isinstance(r.json(), list), f'List is not returned\n{curl}'

    return r.json(), curl


def get_single_object_by_id(object_id, expected_status_code=200):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.get(url)
    curl = curlify.to_curl(r.request)

    assert r.status_code == expected_status_code, f'Status code is incorrect: {r.status_code}\n{curl}'

    return r.json(), curl


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

    assert r.status_code == 200, f'Status code is incorrect: {r.status_code}\n{curl}'
    assert r.json()['id'] is not None, f'Id is not created\n{curl}'
    assert r.json()['name'] == payload['name'], f'Name is incorrect: {r.json()["name"]}\n{curl}'
    assert r.json()['data'] == payload['data'], f'Data is incorrect: {r.json()["data"]}\n{curl}'

    created_id = r.json()['id']

    # make sure that object was created
    single, curl_single = get_single_object_by_id(created_id)
    assert created_id == single['id'], f'Created object is not exist.\n{curl_single}'

    return r.json(), curl


def update_object(object_id, payload):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.put(url, json=payload)
    curl = curlify.to_curl(r.request)

    assert r.status_code == 200, f'Status code is incorrect: {r.status_code}\n{curl}'
    assert r.json()['id'] == object_id, f'Id is incorrect: {r.json()["id"]}\n{curl}'
    assert r.json()['name'] == payload['name'], f'Name is incorrect: {r.json()["name"]}\n{curl}'
    assert r.json()['data'] == payload['data'], f'Data is incorrect: {r.json()["data"]}\n{curl}'

    return r.json(), curl


def update_partial_object(object_id, partial_payload, expected_payload):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.patch(url, json=partial_payload)
    curl = curlify.to_curl(r.request)

    assert r.status_code == 200, f'Status code is incorrect: {r.status_code}\n{curl}'
    assert r.json()['id'] == object_id, f'Id is incorrect: {r.json()["id"]}\n{curl}'
    assert r.json()['name'] == expected_payload['name'], f'Name is incorrect: {r.json()["name"]}\n{curl}'
    assert r.json()['data'] == expected_payload['data'], f'Data is incorrect: {r.json()["data"]}\n{curl}'

    return r.json(), curl


def delete_object(object_id):
    url = f'{BASE_URI}/objects/{object_id}'
    r = requests.delete(url)
    curl = curlify.to_curl(r.request)

    assert r.status_code == 200, f'Status code is incorrect: {r.status_code}\n{curl}\n{curl}'
    assert r.json()['message'] == f'Object with id = {object_id} has been deleted.', \
        f'Message is incorrect: {r.json()["message"]}\n{curl}'

    # make sure that object was deleted
    single, curl = get_single_object_by_id(object_id, expected_status_code=404)
    assert single['error'] == f'Oject with id={object_id} was not found.', f'Object was not deleted\n{curl}'

    return r.json(), curl


get_list, curl_1 = get_all_list()
print(f'List of all objects:\ncurl: {curl_1}, \n {get_list}\n')

get_list_by_id, curl_2 = get_list_by_ids(1, 2, 3)
print(f'List of objects by ids:\ncurl: {curl_2}, \n {get_list_by_id}\n')

single_object, curl_3 = get_single_object_by_id(13)
print(f'Single object:\ncurl: {curl_3}, \n {single_object}\n')

add_obj, curl_4 = add_object('Apple MacBook Pro 17 test', 2024, 3000, 'i9', '1TB')
print(f'Add object:\ncurl: {curl_4}, \n{add_obj}\n')

payload_update = add_obj
update_id = payload_update['id']
del payload_update['id']
del payload_update['createdAt']
payload_update['data']['price'] = 3600
payload_update['data']['color'] = 'silver'

updated_put, curl_5 = update_object(update_id, payload_update)
print(f'Update object:\ncurl: {curl_5}\n{updated_put}\n')

payload_partial = {"name": "Apple MacBook Pro 16 (Updated Name PARTIAL)"}

payload_update['name'] = payload_partial['name']
updated_patch, curl_6 = update_partial_object(update_id, payload_partial, expected_payload=payload_update)

print(f'Partially update object:\ncurl: {curl_6}\n{updated_patch}\n')

delete_obj, curl_7 = delete_object(update_id)
print(f'Delete object:\ncurl: {curl_7}\n{delete_obj}')
