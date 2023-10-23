"""
Unit tests for the Calculator and Database classes.
"""

import unittest
from calculator import Database, Calculator

class TestDatabase(unittest.TestCase):
    """
    Test cases for the Database class.
    """

    def setUp(self):
        """
        Set up a temporary in-memory database for testing.
        """
        self.database = Database(':memory:')

    def test_create_results_table(self):
        """
        Test the create_results_table method.
        """
        self.database.create_results_table()
        # Add assertions to test the behavior

    def test_get_all_results(self):
        """
        Test the get_all_results method.
        """
        self.database.create_results_table()
        # Add test data and assertions

class TestCalculator(unittest.TestCase):
    """
    Test cases for the Calculator class.
    """

    def setUp(self):
        """
        Set up a Calculator instance with a temporary in-memory database.
        """
        self.database = Database(':memory:')
        self.calculator = Calculator(self.database)

    def test_add(self):
        """
        Test the add method of the Calculator class.
        """
        self.calculator.add(2)
        self.assertEqual(self.calculator.get_result(), 2)

    # Add more test methods for the Calculator class

if __name__ == '__main__':
    unittest.main()
