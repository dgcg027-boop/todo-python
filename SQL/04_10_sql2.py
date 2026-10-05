import sqlite3

conn = sqlite3.connect("students.db")
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

print("Все студенты:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE students SET age = ? WHERE name = ?", (21, "Аня"))
conn.commit()

print("\nПосле обновления:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM students WHERE name = ?", ("Борис",))
conn.commit()

print("\nПосле удаления:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

conn.close()