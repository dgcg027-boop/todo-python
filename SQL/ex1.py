import sqlite3

conn = sqlite3.connect("ex1.db")
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

cursor.execute("INSERT INTO students (name, age, city) VALUES (?, ?, ?)", ("Иван", 20, "Москва"))
cursor.execute("INSERT INTO students (name, age, city) VALUES (?, ?, ?)", ("Мария", 22, "Санкт-Петербург"))
cursor.execute("INSERT INTO students (name, age, city) VALUES (?, ?, ?)", ("Пётр", 19, "Москва"))
cursor.execute("INSERT INTO students (name, age, city) VALUES (?, ?, ?)", ("Анна", 21, "Казань"))
conn.commit()

print("Все студенты:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

print("Студенты из Москвы:")
cursor.execute("SELECT * FROM students WHERE city = ?", ("Москва",))
for row in cursor.fetchall():
    print(row)

print("Студенты по возрасту:")
cursor.execute("SELECT * FROM students ORDER BY age")
for row in cursor.fetchall():
    print(row)

conn.close()