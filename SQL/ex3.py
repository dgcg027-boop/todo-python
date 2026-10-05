import sqlite3

conn = sqlite3.connect("ex3.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT, 
        author TEXT,
        year INTEGER
        )
""")
conn.commit()

cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", ("Война и мир", "Лев Толстой", 1869))
cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", ("Преступление и наказание", "Фёдор Достоевский", 1866))
cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", ("Мастер и Маргарита", "Михаил Булгаков", 1967))
cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",("1984", "Джордж Оруэлл", 1949))
conn.commit()

print("Книги, вышедшие после 1900:")
cursor.execute("SELECT * FROM books WHERE year > 1900")
for row in cursor.fetchall():
    print(row)

print("Книги по году:")
cursor.execute("SELECT * FROM books ORDER BY year DESC")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE books SET year = ? WHERE title = ?", (1959, "1984"))
conn.commit()

cursor.execute("DELETE FROM books WHERE title = ?", ("Мастер и Маргарита",))
conn.commit()

print("Все книги:")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()