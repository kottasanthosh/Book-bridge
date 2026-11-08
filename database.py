import sqlite3

DATABASE = "users.db"

def get_connection_db():
    # conncect the DB
    conn = sqlite3.connect(DATABASE)
    # We can access the colums by name
    conn.row_factory = sqlite3.Row
    # Returning the connection object
    return conn