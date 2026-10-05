import sqlite3

conn = sqlite3.connect("join.db")
cursor = conn.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")
conn.commit()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        grade INTEGER
    )
""")
conn.commit()

cursor.execute("INSERT INTO students (name) VALUES (?)", ("Иван",))
cursor.execute("INSERT INTO students (name) VALUES (?)", ("Анна",))
conn.commit()

cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (1, 5))
cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (1, 4))
cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (2, 5))
conn.commit()

cursor.execute("""
    SELECT students.name, grades.grade 
    FROM students
    JOIN grades ON students.id = grades.student_id
""")
for row in cursor.fetchall():
    print(row)

conn.close()