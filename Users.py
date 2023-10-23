import sqlite3

class Calculator:
    def __init__(self, database):
        self.database = database
        self.current_value = 0

    def add(self, value):
        self.current_value += value

    def subtract(self, value):
        self.current_value -= value

    def multiply(self, value):
        self.current_value *= value

    def divide(self, value):
        self.current_value /= value

    def get_result(self):
        return self.current_value

    def save_result(self):
        self.database.execute('INSERT INTO results (value) VALUES (?)', (self.current_value,))
        self.database.commit()

class Database:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def create_results_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY AUTOINCREMENT, value REAL)')

    def get_all_results(self):
        self.cursor.execute('SELECT * FROM results')
        results = []
        for row in self.cursor.fetchall():
            results.append(row[1])
        return results

database = Database('results.sqlite3')

# Create the results table if it doesn't exist
database.create_results_table()

# Create a new calculator object
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
