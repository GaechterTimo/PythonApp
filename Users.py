"""
This is a simple calculator demo application that has external dependencies and interacts with a database.
"""

from typing import List

import sqlite3


class Calculator:
    """A calculator that can perform basic arithmetic operations and save the results to a database."""

    def __init__(self, database: Database):
        self.database = database
        self.current_value = 0

    def add(self, value: float) -> None:
        """Adds a value to the current value."""
        self.current_value += value

    def subtract(self, value: float) -> None:
        """Subtracts a value from the current value."""
        self.current_value -= value

    def multiply(self, value: float) -> None:
        """Multiplies the current value by a value."""
        self.current_value *= value

    def divide(self, value: float) -> None:
        """Divides the current value by a value."""
        if value == 0:
            raise ValueError("Cannot divide by zero")
        self.current_value /= value

    def get_result(self) -> float:
        """Returns the current value."""
        return self.current_value

    def save_result(self) -> None:
        """Saves the current value to the database."""
        self.database.execute('INSERT INTO results (value) VALUES (?)', (self.current_value,))
        self.database.commit()


class Database:
    """A database that stores the results of calculations."""

    def __init__(self, filename: str):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def create_results_table(self) -> None:
        """Creates the results table if it doesn't exist."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL
        )''')

    def get_all_results(self) -> List[float]:
        """Returns a list of all the results in the database."""
        self.cursor.execute('SELECT * FROM results')
        results = []
        for row in self.cursor.fetchall():
            results.append(row[1])
        return results


def main():
    database = Database('results.sqlite3')
    database.create_results_table()

    calculator = Calculator(database)

    # Add two numbers
    calculator.add(2)
    calculator.add(3)

    # Print the result
    print(calculator.get_result())

    # Save the result to the database
    calculator.save_result()

    # Get all results from the database
    results = database.get_all_results()

    # Print the results
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
