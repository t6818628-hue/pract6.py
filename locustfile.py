from locust import HttpUser, task, between
from faker import Faker

fake = Faker()

class BlogUser(HttpUser):
    # Пользователь ждет от 1 до 2 секунд между действиями
    wait_time = between(1, 2)

    @task(3)  # Вес 3: это действие будет выполняться в 3 раза чаще
    def view_posts(self):
        self.client.get("/posts")

    @task(1)  # Вес 1: создание поста происходит реже
    def create_post(self):
        self.client.post("/posts", json={
            "title": fake.sentence(),
            "content": fake.text()
        })      
        #