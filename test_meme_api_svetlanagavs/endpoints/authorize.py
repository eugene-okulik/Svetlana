import os
import requests
import curlify
import allure

from test_meme_api_svetlanagavs.endpoints.base_endpoint import BaseEndpoint


class Authorize(BaseEndpoint):
    @allure.step('Authorize user')
    def authorize(self, name):
        payload = {"name": name}
        self.response = requests.post(f'{self.base_url}/authorize', json=payload)
        self.json = self.response.json()
        self.curl = curlify.to_curl(self.response.request)
        return self.json.get('token')

    @allure.step('Check if token is alive')
    def check_token_is_alive(self, token):
        self.response = requests.get(f'{self.base_url}/authorize/{token}')
        self.curl = curlify.to_curl(self.response.request)
        return self.response.status_code == 200


def get_token(name='svetlana_gavs'):
    auth = Authorize()

    saved_token = os.environ.get('MEME_API_TOKEN')
    if saved_token and auth.check_token_is_alive(saved_token):
        return saved_token

    token = auth.authorize(name)
    os.environ['MEME_API_TOKEN'] = token

    return token
