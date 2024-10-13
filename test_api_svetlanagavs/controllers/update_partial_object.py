import requests
import curlify
import allure

from test_api_svetlanagavs.controllers.base_endpoint_details import BaseEndpointDetails


class UpdatePartialObject(BaseEndpointDetails):
    @allure.step('Update partial object')
    def update_partial_object(self, object_id, partial_payload):
        self.response = requests.patch(f'{self.base_url}/objects/{object_id}', json=partial_payload)
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response
