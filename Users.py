import sqlite3

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Database:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def create_users_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )''')

    def insert_user(self, user):
        self.cursor.execute('''INSERT INTO users (name, email) 
            VALUES (?, ?)''',
            (user.name, user.email))
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        users = []
        for row in self.cursor.fetchall():
            users.append(User(row[0], row[1], row[2]))
        return users

database = Database('users.sqlite3')

# Create the users table if it doesn't exist
database.create_users_table()

# Insert a new user
user = User(None, 'Bard', 'bard@google.com')
database.insert_user(user)

# Get all users
users = database.get_all_users()

# Print the names of all users
for user in users:
    print(user.name)
