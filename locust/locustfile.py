from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Set wait time between tasks

    @task
    def visit_homepage(self):
        self.client.get("/")

    @task
    def perform_search(self):
        self.client.get("/search?query=test")

    # Add more tasks as needed

    def on_start(self):
        # Actions to perform when a user starts a test

    def on_stop(self):
        # Actions to perform when a user stops a test
