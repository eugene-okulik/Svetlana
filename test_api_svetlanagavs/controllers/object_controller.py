from test_api_svetlanagavs.controllers.base_endpoint import BaseEndpoint, BaseEndpointDetails
import requests
import curlify
import allure


class GetAllList(BaseEndpoint):
    @allure.step('Get all list')
    def get_all_list(self):
        self.response = requests.get(f'{self.base_url}/objects')
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response


class GetListByIds(BaseEndpoint):
    @allure.step('Get list by ids')
    def get_list_by_ids(self, *args):
        url = f'{self.base_url}/objects?'
        for i in args:
            url += f'id={i}&'
        self.response = requests.get(url)
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response


class GetSingleObjectById(BaseEndpointDetails):
    @allure.step('Get single object by id')
    def get_single_object_by_id(self, object_id):
        self.response = requests.get(f'{self.base_url}/objects/{object_id}')
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response


class AddObject(BaseEndpointDetails):
    @allure.step('Add object')
    def add_object(self, name, year, price, cpu_model, hard_disk_size):
        payload = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": cpu_model,
                "Hard disk size": hard_disk_size
            }
        }
        self.response = requests.post(f'{self.base_url}/objects', json=payload)
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response


class UpdateObject(BaseEndpointDetails):
    @allure.step('Update object')
    def update_object(self, object_id, payload):
        self.response = requests.put(f'{self.base_url}/objects/{object_id}', json=payload)
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response


class UpdatePartialObject(BaseEndpointDetails):
    @allure.step('Update partial object')
    def update_partial_object(self, object_id, partial_payload):
        self.response = requests.patch(f'{self.base_url}/objects/{object_id}', json=partial_payload)
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response


class DeleteObject(BaseEndpoint):
    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.base_url}/objects/{object_id}')
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response
