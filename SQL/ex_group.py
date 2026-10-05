import sqlite3

conn = sqlite3.connect("join.db")
cursor = conn.cursor()

print("Количесво студентов:")
cursor.execute("SELECT COUNT(*) FROM students")
for row in cursor.fetchall():
    print(row)

print("Количество оценок у student.id:")
cursor.execute("SELECT student_id, COUNT(*) FROM grades GROUP BY student_id")
for row in cursor.fetchall():
    print(row)

print("Количество оценок у каждого студента:")
cursor.execute("""
    SELECT students.name, COUNT(*)
    FROM students
    JOIN grades ON students.id = grades.student_id
    GROUP BY students.id
""")
for row in cursor.fetchall():
    print(row)

print("Имя студена и средняя оценка:")
cursor.execute("""
    SELECT students.name, AVG(grades.grade)
    FROM students
    JOIN grades ON students.id = grades.student_id
    GROUP BY students.id
""")
for row in cursor.fetchall():
    print(row)

conn.close()