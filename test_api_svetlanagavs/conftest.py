import pytest

from test_api_svetlanagavs.controllers import create_object
from test_api_svetlanagavs.controllers import delete_object
from test_api_svetlanagavs.controllers import get_by_id_object
from test_api_svetlanagavs.controllers import get_list_by_ids_object
from test_api_svetlanagavs.controllers import get_entire_list_object
from test_api_svetlanagavs.controllers import update_object
from test_api_svetlanagavs.controllers import update_partial_object

from test_api_svetlanagavs.controllers.base_data_object import ObjectData


@pytest.fixture()
def get_all_list():
    return get_entire_list_object.GetAllList()


@pytest.fixture()
def get_list_by_ids():
    return get_list_by_ids_object.GetListByIds()


@pytest.fixture()
def get_single_object_by_id():
    return get_by_id_object.GetSingleObjectById()


@pytest.fixture()
def partial_update_object():
    return update_partial_object.UpdatePartialObject()


@pytest.fixture()
def delete_by_id_object():
    return delete_object.DeleteObject()


@pytest.fixture()
def create_one_object():
    return create_object.AddObject()


@pytest.fixture()
def update_by_id_object():
    return update_object.UpdateObject()


@pytest.fixture()
def add_delete_object(request, create_one_object, delete_by_id_object):
    name, year, price, cpu_model, hard_disk_size, include_test_data = request.param

    create_one_object.add_object(name, year, price, cpu_model, hard_disk_size)
    object_id = create_one_object.json['id']

    if include_test_data:
        yield create_one_object, ObjectData(name, year, price, cpu_model, hard_disk_size)
    else:
        yield create_one_object

    delete_by_id_object.delete_object(object_id)
