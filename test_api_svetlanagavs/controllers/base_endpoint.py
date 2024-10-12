import allure


class ObjectData:
    def __init__(self, name, year, price, cpu_model, hard_disk_size):
        self.name = name
        self.year = year
        self.price = price
        self.cpu_model = cpu_model
        self.hard_disk_size = hard_disk_size


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


class BaseEndpointDetails(BaseEndpoint):
    @allure.step('Check id of the object is correct')
    def check_id(self, object_id):
        assert self.json['id'] == object_id, f'Expected id is {object_id}, but got {self.json["id"]}.\n{self.curl}'

    @allure.step('Check name of the object is correct')
    def check_object_name(self, object_name):
        assert self.json['name'] == object_name, (
            f'Expected name is {object_name}, but got {self.json["name"]}.\n{self.curl}'
        )

    @allure.step('Check data of the object is correct: Year, Price, CPU model, Hard disk size')
    def check_object_data_details(self, year, price, cpu_model, hard_disk_size):
        assert self.json['data']['year'] == year, (
            f'Expected year is {year}, but got {self.json["data"]["year"]}.\n{self.curl}'
        )
        assert self.json['data']['price'] == price, (
            f'Expected price is {price}, but got {self.json["data"]["price"]}.\n{self.curl}'
        )
        assert self.json['data']['CPU model'] == cpu_model, (
            f'Expected CPU model is {cpu_model}, but got {self.json["data"]["CPU model"]}.\n{self.curl}'
        )
        assert self.json['data']['Hard disk size'] == hard_disk_size, (
            f'Expected Hard disk size is {hard_disk_size}, but got {self.json["data"]["Hard disk size"]}.\n{self.curl}'
        )

    @allure.step('Check data of the object is correct')
    def check_object_entire_data(self, expected_data):
        assert self.json['data'] == expected_data, (
            f"Expected data is {expected_data}, but got {self.json['data']}.\n{self.curl}"
        )
