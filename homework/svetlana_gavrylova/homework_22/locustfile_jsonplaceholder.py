import random

from locust import task, HttpUser


class RestApiUser(HttpUser):
    host = 'https://jsonplaceholder.typicode.com'
    user_posts = []

    def on_start(self):
        response = self.client.get('/posts?userId=1')
        if response.status_code == 200:
            self.user_posts = response.json()

    def on_stop(self):
        self.user_posts = []

    @task(3)
    def get_all_posts(self):
        self.client.get('/posts')

    @task(5)
    def get_single_post(self):
        post_id = random.randint(1, 100)
        self.client.get(f'/posts/{post_id}')

    @task(2)
    def get_posts_by_user(self):
        self.client.get('/posts?userId=1')

    @task(1)
    def create_and_delete_post(self):
        response = self.client.post(
            '/posts',
            json={
                "title": "Temporary Post",
                "body": "This post will be deleted",
                "userId": 1
            }
        )
        if response.status_code == 201:
            new_id = response.json().get('id')
            if new_id:
                self.client.delete(f'/posts/{new_id}')

    @task(1)
    def update_post(self):
        post_id = random.randint(1, 100)
        self.client.put(
            f'/posts/{post_id}',
            json={
                "title": "Updated Post Title",
                "body": "Updated post body",
                "userId": 1
            }
        )
