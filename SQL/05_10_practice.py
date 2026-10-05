import sqlite3

conn = sqlite3.connect("practice.db")
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
conn.commit()

print("ВСе книги:")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()