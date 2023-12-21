from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Dummy username and password
USERNAME = 'admin'
PASSWORD = 'password'

# Function to create a connection to the SQLite database
def create_connection():
    return sqlite3.connect('my_database.db')

# Function to create the Users table if it doesn't exist
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

# Insert data into the table
    sqlite3.Cursor.execute("INSERT INTO users VALUES (?, ?)", ('keni', '1234'))

    # Commit the changes and close the connection
    sqlite3.connect.commit()
    sqlite3.connect.close()


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    connection = create_connection()
    cursor = connection.cursor()

    # Check if the user with the given username and password exists
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    connection.close()

    if user:
        return render_template('welcome.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
