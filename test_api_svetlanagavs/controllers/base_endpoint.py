import allure


class BaseEndpoint:
    base_url = 'https://api.restful-api.dev'
    response = None
    json = None
    curl = None

    @allure.step('Check status code is correct')
    def check_status_code(self, expected_status_code=200):
        assert self.response.status_code == expected_status_code, (
            f'Expected {expected_status_code} status code, but got {self.response.status_code}.\n{self.curl}'
        )

    @allure.step('Check instance of the object is correct')
    def check_instance(self, object_instance):
        assert isinstance(self.json, object_instance), (
            f'Expected instance is {object_instance}, but got {type(self.json)}.\n{self.curl}'
        )

    @allure.step('Check the object is not empty')
    def check_object_is_not_empty(self):
        assert len(self.json) > 0, f'Expected object is not empty, but got empty object.\n{self.curl}'
