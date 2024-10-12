import requests
import curlify
import allure

from test_api_svetlanagavs.controllers.base_endpoint_details import BaseEndpointDetails


class UpdateObject(BaseEndpointDetails):
    @allure.step('Update object')
    def update_object(self, object_id, payload):
        self.response = requests.put(f'{self.base_url}/objects/{object_id}', json=payload)
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response
