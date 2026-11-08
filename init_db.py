from database import get_connection_db

conn = get_connection_db()

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS USERS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database users created successfully!")