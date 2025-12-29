import sqlite3

conn = sqlite3.connect("career.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    skills TEXT,
    career TEXT,
    skill_gap TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
