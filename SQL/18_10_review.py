import sqlite3

conn = sqlite3.connect("departments.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    name TEXT
    )
""")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary INTEGER,
    department_id INTEGER
    )
""")
conn.commit()

cursor.execute("INSERT INTO departments (name) VALUES (?)", ("IT",))
cursor.execute("INSERT INTO departments (name) VALUES (?)", ("HR",))
cursor.execute("INSERT INTO departments (name) VALUES (?)", ("Sales",))
conn.commit()

cursor.execute("INSERT INTO employees (name, age, salary, department_id) VALUES (?, ?, ?, ?)", ("Иван", 25, 50000, 1))
cursor.execute("INSERT INTO employees (name, age, salary, department_id) VALUES (?, ?, ?, ?)", ("Мария", 30, 70000, 1))
cursor.execute("INSERT INTO employees (name, age, salary, department_id) VALUES (?, ?, ?, ?)", ("Пётр", 40, 60000, 2))
cursor.execute("INSERT INTO employees (name, age, salary, department_id) VALUES (?, ?, ?, ?)", ("Анна", 28, 55000, 3))
conn.commit()

print("Все сотрудники:")
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

print("Имя сотрудника - отдел:")
cursor.execute("""
    SELECT employees.name, departments.name
    FROM employees
    JOIN departments ON departments.id = employees.department_id
""")
for row in cursor.fetchall():
    print(row)

print("Сотруднки с ЗП >55000")
cursor.execute("""
    SELECT employees.name, departments.name, employees.salary
    FROM employees
    JOIN departments ON departments.id = employees.department_id
    WHERE salary > 55000
""")
for row in cursor.fetchall():
    print(row)

print("Отдел и количесвто сотрудников:")
cursor.execute("""
    SELECT departments.name, COUNT(*)
    FROM departments
    JOIN employees ON departments.id = employees.department_id
    GROUP BY departments.name
""")
for row in cursor.fetchall():
    print(row)

print("Отдел и средняя ЗП:")
cursor.execute("""
    SELECT departments.name, AVG(employees.salary)
    FROM departments
    JOIN employees ON departments.id = employees.department_id
    GROUP BY departments.name
    """)
for row in cursor.fetchall():
    print(row)

print("Все сотркдники по ЗП убыванию")
cursor.execute("""
    SELECT * FROM employees
    ORDER BY employees.salary DESC
""")
for row in cursor.fetchall():
    print(row)