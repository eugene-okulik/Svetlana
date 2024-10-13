import requests
import curlify
import allure

from test_api_svetlanagavs.controllers.base_endpoint import BaseEndpoint


class GetAllList(BaseEndpoint):
    @allure.step('Get all list')
    def get_all_list(self):
        self.response = requests.get(f'{self.base_url}/objects')
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response
