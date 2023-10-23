from locust import HttpUser, task, between

class CalculatorUser(HttpUser):
    wait_time = between(1, 5)  # Set wait time between tasks

    @task
    def add_numbers(self):
        response = self.client.get("/add?value=5")  # Simulate adding numbers
        if response.status_code == 200:
            self.locust.log_success("add_numbers", response.elapsed.total_seconds())
        else:
            self.locust.log_failure("add_numbers", response.text)

    @task
    def subtract_numbers(self):
        response = self.client.get("/subtract?value=2")  # Simulate subtracting numbers
        if response.status_code == 200:
            self.locust.log_success("subtract_numbers", response.elapsed.total_seconds())
        else:
            self.locust.log_failure("subtract_numbers", response.text)

    @task
    def multiply_numbers(self):
        response = self.client.get("/multiply?value=3")  # Simulate multiplying numbers
        if response.status_code == 200:
            self.locust.log_success("multiply_numbers", response.elapsed.total_seconds())
        else:
            self.locust.log_failure("multiply_numbers", response.text)

    @task
    def divide_numbers(self):
        response = self.client.get("/divide?value=2")  # Simulate dividing numbers
        if response.status_code == 200:
            self.locust.log_success("divide_numbers", response.elapsed.total_seconds())
        else:
            self.locust.log_failure("divide_numbers", response.text)

    def on_start(self):
        # Actions to perform when a user starts a test
        self.client.get("/")  # Visit the calculator's homepage

    def on_stop(self):
        # Actions to perform when a user stops a test
        pass  # You can add actions here if needed
