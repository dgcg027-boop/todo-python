import sqlite3

conn = sqlite3.connect("ex4.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
    )
""")
conn.commit()

cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", ("Ноутбук", 50000, 10))
cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", ("Мышь", 1500, 50))
cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", ("Клавиатура", 3000, 0))
conn.commit()

print("Товары дороже 1000:")
cursor.execute("SELECT * FROM products WHERE price > 1000")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE products SET price = ? WHERE name = ?", (2000, "Мышь"))
conn.commit()

cursor.execute("DELETE FROM products WHERE quantity = 0")
conn.commit()

print("Все товары:")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

conn.close()