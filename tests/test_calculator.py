# In your test script (e.g., test_calculator.py)

# Import the necessary modules
import unittest
from calculator import Database, Calculator

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
        result = self.calculator.get_result()
        print(f"Addition Result: {result}")
        self.assertEqual(result, 2)

    def test_subtract(self):
        """
        Test the subtract method of the Calculator class.
        """
        self.calculator.add(5)  # Start with a value of 5
        self.calculator.subtract(2)
        result = self.calculator.get_result()
        print(f"Subtraction Result: {result}")
        self.assertEqual(result, 3)

    def test_multiply(self):
        """
        Test the multiply method of the Calculator class.
        """
        self.calculator.add(3)  # Start with a value of 3
        self.calculator.multiply(4)
        result = self.calculator.get_result()
        print(f"Multiplication Result: {result}")
        self.assertEqual(result, 12)

    def test_divide(self):
        """
        Test the divide method of the Calculator class.
        """
        self.calculator.add(10)  # Start with a value of 10
        self.calculator.divide(2)
        result = self.calculator.get_result()
        print(f"Division Result: {result}")
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
