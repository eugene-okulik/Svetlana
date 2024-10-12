import requests
import curlify
import allure

from test_api_svetlanagavs.controllers.base_endpoint_details import BaseEndpointDetails


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
