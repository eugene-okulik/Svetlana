import requests
import curlify
import allure

from test_api_svetlanagavs.controllers.base_endpoint_details import BaseEndpointDetails


class GetSingleObjectById(BaseEndpointDetails):
    error_message = None

    @allure.step('Get single object by id')
    def get_single_object_by_id(self, object_id):
        self.response = requests.get(f'{self.base_url}/objects/{object_id}')
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response

    @allure.step('Check error message')
    def check_error_message(self, object_id):
        assert self.json['error'] == f'Oject with id={object_id} was not found.', \
            f'Object was not deleted\n{self.curl}'
