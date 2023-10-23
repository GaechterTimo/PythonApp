from locust import HttpUser, task

class CalculatorUser(HttpUser):
    @task
    def add(self):
        self.client.post("/add", {"value1": 2, "value2": 3})

    @task
    def subtract(self):
        self.client.post("/subtract", {"value1": 2, "value2": 3})

    @task
    def multiply(self):
        self.client.post("/multiply", {"value1": 2, "value2": 3})

    @task
    def divide(self):
        self.client.post("/divide", {"value1": 2, "value2": 3})

if __name__ == "__main__":
    run_single_user()
