import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    name TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    author_id INTEGER,
    title TEXT,
    year INTEGER
    )
""")
conn.commit()

cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Толстой",))
cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Достоевский",))
cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Булгаков",))
cursor.execute("INSERT INTO books (author_id, title, year) VALUES (?, ?, ?)",(1, "Война и мир", 1869))
cursor.execute("INSERT INTO books (author_id, title, year) VALUES (?, ?, ?)",(1, "Анна Каренина", 1877))
cursor.execute("INSERT INTO books (author_id, title, year) VALUES (?, ?, ?)",(2, "Преступление и наказание", 1866))
cursor.execute("INSERT INTO books (author_id, title, year) VALUES (?, ?, ?)",(3, "Мастер и Маргарита", 1967))
conn.commit()

print("Автор - книга:")
cursor.execute("""
    SELECT authors.name, books.title
    FROM authors
    JOIN books ON authors.id = books.author_id
""")
for row in cursor.fetchall():
    print(row)

print("Автор и количесвто его книг:")
cursor.execute("""
    SELECT authors.name, COUNT(*)
    FROM authors
    JOIN books ON authors.id = books.author_id
    GROUP BY authors.name
""")
for row in cursor.fetchall():
    print(row)

print("Книги после 1900 года:")
cursor.execute("""
    SELECT authors.name, books.title 
    FROM authors
    JOIN books ON authors.id = books.author_id
    WHERE books.year > 1900
""")
for row in cursor.fetchall():
    print(row)

print("Все книги отсортированные по году")
cursor.execute("""
    SELECT authors.name, books.title
    FROM authors
    JOIN books ON authors.id = books.author_id
    ORDER BY books.year
""")
for row in cursor.fetchall():
    print(row)

conn.close()