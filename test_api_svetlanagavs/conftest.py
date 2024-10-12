import pytest

from test_api_svetlanagavs.controllers import object_controller
from test_api_svetlanagavs.controllers.base_endpoint import ObjectData


@pytest.fixture()
def get_all_list():
    return object_controller.GetAllList()


@pytest.fixture()
def get_list_by_ids():
    return object_controller.GetListByIds()


@pytest.fixture()
def get_single_object_by_id():
    return object_controller.GetSingleObjectById()


@pytest.fixture()
def partial_update_object():
    return object_controller.UpdatePartialObject()


@pytest.fixture()
def delete_object():
    return object_controller.DeleteObject()


@pytest.fixture()
def create_object():
    return object_controller.AddObject()


@pytest.fixture()
def update_object():
    return object_controller.UpdateObject()


@pytest.fixture()
def add_object(request, create_object, delete_object):
    name, year, price, cpu_model, hard_disk_size, include_test_data = request.param

    create_object.add_object(name, year, price, cpu_model, hard_disk_size)
    object_id = create_object.json['id']

    if include_test_data:
        yield create_object, ObjectData(name, year, price, cpu_model, hard_disk_size)
    else:
        yield create_object

    delete_object.delete_object(object_id)
