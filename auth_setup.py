import sqlite3

conn = sqlite3.connect("career.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS auth_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
conn.close()

print("Auth users table created")
