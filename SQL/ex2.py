import sqlite3

conn = sqlite3.connect("ex2.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT
    )
""")
conn.commit()

cursor.execute("INSERT INTO students (name, age, city) VALUES(?, ?, ?)", ("Иван", 20, "Москва"))
cursor.execute("INSERT INTO students (name, age, city) VALUES(?, ?, ?)", ("Мария", 22, "Санкт-Петербург"))
cursor.execute("INSERT INTO students (name, age, city) VALUES(?, ?, ?)", ("Пётр", 19, "Москва"))
conn.commit()

cursor.execute("UPDATE students SET age = ? WHERE name = ?", (21, "Иван"))
conn.commit()

print("Все студенты после обновления:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM students WHERE name = ?", ("Пётр",))
conn.commit()

print("Все студенты после удаления:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)
conn.close()