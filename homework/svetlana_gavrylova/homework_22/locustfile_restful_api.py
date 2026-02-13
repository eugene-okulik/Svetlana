from locust import task, HttpUser


class RestApiUser(HttpUser):
    host = 'https://api.restful-api.dev'
    object_id = None

    def on_start(self):
        response = self.client.post(
            '/objects',
            json={
                "name": "Apple MacBook Pro 14 locust",
                "data": {
                    "year": 2022,
                    "price": 2000,
                    "CPU model": "i7",
                    "Hard disk size": "1TB"
                }
            }
        )
        if response.status_code == 200:
            self.object_id = response.json().get('id')

    @task(3)
    def get_all_objects(self):
        self.client.get('/objects')

    @task(5)
    def get_single_object(self):
        if self.object_id:
            self.client.get(f'/objects/{self.object_id}')

    @task(2)
    def get_objects_by_ids(self):
        self.client.get('/objects?id=1&id=2&id=3')

    @task(1)
    def create_and_delete_object(self):
        response = self.client.post(
            '/objects',
            json={
                "name": "Locust Test Object",
                "data": {
                    "year": 2024,
                    "price": 1500,
                    "CPU model": "i5",
                    "Hard disk size": "512GB"
                }
            }
        )
        if response.status_code == 200:
            new_id = response.json().get('id')
            if new_id:
                self.client.delete(f'/objects/{new_id}')

    @task(1)
    def update_object(self):
        if self.object_id:
            self.client.put(
                f'/objects/{self.object_id}',
                json={
                    "name": "Apple MacBook Pro 14 Updated",
                    "data": {
                        "year": 2023,
                        "price": 2500,
                        "CPU model": "i9",
                        "Hard disk size": "2TB"
                    }
                }
            )

    def on_stop(self):
        if self.object_id:
            self.client.delete(f'/objects/{self.object_id}')
