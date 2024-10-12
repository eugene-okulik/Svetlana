import pytest


def test_get_list(get_all_list):
    get_all_list.get_all_list()
    get_all_list.check_status_code()


def test_get_list_by_ids(get_list_by_ids):
    get_list_by_ids.get_list_by_ids(1, 2, 3)
    get_list_by_ids.check_status_code()
    get_list_by_ids.check_instance(list)
    get_list_by_ids.check_object_is_not_empty()


@pytest.mark.parametrize(
    'add_delete_object', [('Apple MacBook Pro 14 get id', 2022, 2000, 'i7', '1TB', True)], indirect=True
)
def test_get_single_object_by_id(add_delete_object, get_single_object_by_id):
    created_object, test_data = add_delete_object
    object_id = created_object.json['id']

    get_single_object_by_id.get_single_object_by_id(object_id)
    get_single_object_by_id.check_status_code()
    get_single_object_by_id.check_id(object_id)


@pytest.mark.parametrize(
    'add_delete_object',
    [
        ('Apple MacBook Pro 14 test', 2022, 2000, 'i7', '1TB', True),
        ('Apple MacBook Pro 15 test', 2023, 2500, 'i8', '2TB', True),
        ('Apple MacBook Pro 16 test', 2024, 3000, 'i9', '3TB', True),
    ],
    indirect=True
)
def test_add_object(add_delete_object):
    created_object, test_data = add_delete_object
    object_id = created_object.json['id']

    created_object.check_status_code()
    created_object.check_instance(dict)
    created_object.check_object_is_not_empty()
    created_object.check_id(object_id)
    created_object.check_object_name(test_data.name)
    created_object.check_object_data_details(
        test_data.year, test_data.price, test_data.cpu_model, test_data.hard_disk_size
    )


@pytest.mark.parametrize(
    'add_delete_object', [('Apple MacBook Pro 14 update', 2022, 2000, 'i7', '1TB', False)], indirect=True
)
def test_update_object(add_delete_object, update_by_id_object):
    created_object = add_delete_object
    payload_update = created_object.json

    update_id = payload_update['id']
    del payload_update['id']
    del payload_update['createdAt']
    payload_update['data']['price'] = 3600
    payload_update['data']['color'] = 'silver'

    update_by_id_object.update_object(update_id, payload_update)
    update_by_id_object.check_status_code()
    update_by_id_object.check_id(update_id)
    update_by_id_object.check_instance(dict)
    update_by_id_object.check_object_is_not_empty()
    update_by_id_object.check_object_name(payload_update['name'])
    update_by_id_object.check_object_entire_data(payload_update['data'])


@pytest.mark.parametrize(
    'add_delete_object', [('Apple MacBook Pro 14 partial update', 2022, 2000, 'i7', '1TB', False)], indirect=True
)
def test_update_partial_object(add_delete_object, partial_update_object):
    created_object = add_delete_object
    payload_update = created_object.json
    # update partial object
    payload_partial = {"name": "Apple MacBook Pro 16 (Updated Name PARTIAL)"}
    payload_update['name'] = payload_partial['name']

    partial_update_object.update_partial_object(payload_update['id'], payload_partial)
    partial_update_object.check_status_code()
    partial_update_object.check_id(payload_update['id'])
    partial_update_object.check_instance(dict)
    partial_update_object.check_object_is_not_empty()
    partial_update_object.check_object_name(payload_update['name'])
    partial_update_object.check_object_entire_data(payload_update['data'])


@pytest.mark.parametrize(
    'add_delete_object', [('Apple MacBook Pro 14 delete', 2022, 2000, 'i7', '1TB', False)], indirect=True
)
def test_delete_object(add_delete_object, get_single_object_by_id, delete_by_id_object):
    created_object = add_delete_object
    object_id = created_object.json['id']

    delete_by_id_object.delete_object(object_id)
    delete_by_id_object.check_status_code()
    delete_by_id_object.check_delete_message(object_id)
    get_single_object_by_id.get_single_object_by_id(object_id)
    get_single_object_by_id.check_status_code(404)
    get_single_object_by_id.check_error_message(object_id)
