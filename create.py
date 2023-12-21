import sqlite3

def create_database():
    # Connect to the database
    conn = sqlite3.connect('my_database.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table
    cursor.execute("""
    CREATE TABLE users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    """)

    # Insert data into the table
    cursor.execute("INSERT INTO users VALUES (?, ?)", ('keni', '1234'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()