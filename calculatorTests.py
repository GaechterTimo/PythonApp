import unittest
from calculator import Database, Calculator

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database(':memory:')  # Use an in-memory database for testing

    def test_create_results_table(self):
        self.database.create_results_table()
        # Add assertions to test the behavior

    def test_get_all_results(self):
        self.database.create_results_table()
        # Add test data and assertions

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.database = Database(':memory:')
        self.calculator = Calculator(self.database)

    def test_add(self):
        self.calculator.add(2)
        self.assertEqual(self.calculator.get_result(), 2)

    # Add more test methods for the Calculator class

if __name__ == '__main__':
    unittest.main()
