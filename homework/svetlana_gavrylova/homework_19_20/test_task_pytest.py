import pytest
import task_rest_api_controller
import allure


class ObjectData:
    def __init__(self, name, year, price, cpu_model, hard_disk_size):
        self.name = name
        self.year = year
        self.price = price
        self.cpu_model = cpu_model
        self.hard_disk_size = hard_disk_size


@pytest.fixture
def add_object(request):
    name, year, price, cpu_model, hard_disk_size, include_test_data = request.param
    response, r_curl = task_rest_api_controller.add_object(name, year, price, cpu_model, hard_disk_size)

    assert response.status_code == 200, f'Status code is incorrect: {response.status_code}\n{r_curl}'

    if include_test_data:
        yield response.json(), r_curl, ObjectData(name, year, price, cpu_model, hard_disk_size)
    else:
        yield response.json(), r_curl

    task_rest_api_controller.delete_object(response.json()['id'])


@pytest.fixture(scope='session')
def start_complete():
    print('Start testing...')
    yield
    print('\nTesting completed.')


@pytest.fixture
def before_each():
    print('\nBefore test...')
    yield
    print('\nAfter test.')


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Создание поста')
@pytest.mark.critical
@pytest.mark.parametrize(
    'add_object',
    [
        ('Apple MacBook Pro 14 test', 2022, 2000, 'i7', '1TB', True),
        ('Apple MacBook Pro 15 test', 2023, 2500, 'i8', '2TB', True),
        ('Apple MacBook Pro 16 test', 2024, 3000, 'i9', '3TB', True),
    ],
    indirect=True
)
def test_add_object(add_object, start_complete, before_each):
    r_json, r_curl, test_data = add_object
    assert r_json['id'] is not None, f'Id is not created\n{r_curl}'
    assert r_json['name'] == test_data.name, f'Name is incorrect: {r_json["name"]}\n{r_curl}'
    assert r_json['data']['year'] == test_data.year, f'Year is incorrect: {r_json["data"]["year"]}\n{r_curl}'
    assert r_json['data']['price'] == test_data.price, f'Price is incorrect: {r_json["data"]["price"]}\n{r_curl}'
    assert r_json['data']['CPU model'] == test_data.cpu_model, \
        f'CPU model is incorrect: {r_json["data"]["CPU model"]}\n{r_curl}'


@allure.feature('Informative')
@allure.story('Get posts')
@allure.title('Получение поста по идентификатору')
@pytest.mark.parametrize('add_object', [('Apple MacBook Pro 14 get id', 2022, 2000, 'i7', '1TB', False)], indirect=True)
def test_get_single_object_by_id(add_object, before_each):
    r_json, _ = add_object
    # get single object by id
    single, curl = task_rest_api_controller.get_single_object_by_id(r_json['id'])
    assert single.status_code == 200, f'Status code is incorrect: {single.status_code}\n{curl}'
    assert single.json()['id'] == r_json['id'], f'Id is incorrect: {single.json()["id"]}\n{curl}'


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Полное обновление поста')
@pytest.mark.medium
@pytest.mark.parametrize('add_object', [('Apple MacBook Pro 14 update', 2022, 2000, 'i7', '1TB', False)], indirect=True)
def test_update_object(add_object, before_each):
    r_json, _ = add_object
    # update object
    payload_update = r_json
    update_id = payload_update['id']
    del payload_update['id']
    del payload_update['createdAt']
    payload_update['data']['price'] = 3600
    payload_update['data']['color'] = 'silver'

    updated_put, r_curl = task_rest_api_controller.update_object(update_id, payload_update)
    updated_json = updated_put.json()

    assert updated_put.status_code == 200, f'Status code is incorrect: {updated_put.status_code}\n{r_curl}'
    assert updated_json['id'] == update_id, f'Id is incorrect: {updated_json["id"]}\n{r_curl}'
    assert updated_json['name'] == payload_update['name'], f'Name is incorrect: {updated_json["name"]}\n{r_curl}'
    assert updated_json['data'] == payload_update['data'], f'Data is incorrect: {updated_json["data"]}\n{r_curl}'


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Порционное обновление поста')
@pytest.mark.parametrize(
    'add_object', [('Apple MacBook Pro 14 partial update', 2022, 2000, 'i7', '1TB', False)], indirect=True
)
def test_update_partial_object(add_object, before_each):
    r_json, _ = add_object
    payload_update = r_json
    # update partial object
    payload_partial = {"name": "Apple MacBook Pro 16 (Updated Name PARTIAL)"}
    payload_update['name'] = payload_partial['name']

    updated_patch, r_curl = task_rest_api_controller.update_partial_object(
        payload_update['id'], payload_update
    )

    updated_json = updated_patch.json()
    assert updated_patch.status_code == 200, f'Status code is incorrect: {updated_patch.status_code}\n{r_curl}'
    assert updated_json['id'] == payload_update['id'], f'Id is incorrect: {updated_json["id"]}\n{r_curl}'
    assert updated_json['name'] == payload_partial['name'], f'Name is incorrect: {updated_json["name"]}\n{r_curl}'
    assert updated_json['data'] == payload_update['data'], f'Data is incorrect: {updated_json["data"]}\n{r_curl}'


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Удаление поста')
@pytest.mark.parametrize('add_object', [('Apple MacBook Pro 14 delete', 2022, 2000, 'i7', '1TB', False)], indirect=True)
def test_delete_object(add_object, before_each):
    r_json, _ = add_object
    # delete object
    delete_response, r_curl = task_rest_api_controller.delete_object(r_json['id'])
    assert delete_response.status_code == 200, f'Status code is incorrect: {delete_response.status_code}\n{r_curl}'
    assert delete_response.json()['message'] == f'Object with id = {r_json["id"]} has been deleted.', \
        f'Message is incorrect: {delete_response.json()["message"]}\n{r_curl}'
    # make sure that object was deleted
    single, curl = task_rest_api_controller.get_single_object_by_id(r_json['id'])
    assert single.status_code == 404, f'Status code is incorrect: {delete_response.status_code}\n{curl}'
    assert single.json()['error'] == f'Oject with id={r_json["id"]} was not found.', f'Object was not deleted\n{curl}'


@allure.feature('Informative')
@allure.story('Get posts')
@allure.title('Получение всех постов')
def test_get_list(before_each):
    get_list, curl = task_rest_api_controller.get_all_list()

    assert get_list.status_code == 200, f'Status code is incorrect: {get_list.status_code}\n{curl}'
    assert isinstance(get_list.json(), list), f'List is not returned\n{curl}'
    assert len(get_list.json()) > 0, f'List is empty\n{curl}'


@allure.feature('Informative')
@allure.story('Get posts')
@allure.title('Получение постов по идентификаторам')
def test_get_list_by_ids(before_each):
    get_list_by_id, curl = task_rest_api_controller.get_list_by_ids(1, 2, 3)

    assert get_list_by_id.status_code == 200, f'Status code is incorrect: {get_list_by_id.status_code}\n{curl}'
    assert isinstance(get_list_by_id.json(), list), f'List is not returned\n{curl}'
    assert len(get_list_by_id.json()) > 0, f'List is empty\n{curl}'
