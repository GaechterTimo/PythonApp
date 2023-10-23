from locust import HttpUser, task, between

class CalculatorUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def add_operation(self):
        self.client.get("/add?value=2")

    @task
    def subtract_operation(self):
        self.client.get("/subtract?value=2")
