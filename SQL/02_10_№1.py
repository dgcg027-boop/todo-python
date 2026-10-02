import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")
conn.commit()

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Степан", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Аня", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Борис", 22))
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()