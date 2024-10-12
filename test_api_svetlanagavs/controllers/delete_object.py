import requests
import curlify
import allure

from test_api_svetlanagavs.controllers.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    del_message = None

    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.base_url}/objects/{object_id}')
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)

        return self.response

    @allure.step('Check delete message')
    def check_delete_message(self, object_id):
        assert self.json['message'] == f'Object with id = {object_id} has been deleted.', \
            f"Message is incorrect: {self.json['message']}\n{self.curl}"
