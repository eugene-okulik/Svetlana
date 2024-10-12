import requests
import curlify
import allure

from test_api_svetlanagavs.controllers.base_endpoint import BaseEndpoint


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
