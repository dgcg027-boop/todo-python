import sqlite3

conn = sqlite3.connect("review.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
    )
""")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY, 
    customer_id INTEGER,
    product TEXT,
    price INTEGER
    )
""")
conn.commit()

cursor.execute("INSERT INTO customers (name, city) VALUES (?, ?)", ("Иван", "Москва"))
cursor.execute("INSERT INTO customers (name, city) VALUES (?, ?)", ("Мария", "Санкт-Петербург"))
cursor.execute("INSERT INTO customers (name, city) VALUES (?, ?)", ("Пётр", "Казань"))
cursor.execute("INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)", (1, "Ноутбук", 50000))
cursor.execute("INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)", (1, "Мышь", 1500))
cursor.execute("INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)", (2, "Клавиатура", 3000))
cursor.execute("INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)", (3, "Монитор", 20000))
conn.commit()

print("Все клиенты:")
cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():
    print(row)

print("Все заказы:")
cursor.execute("SELECT * FROM orders")
for row in cursor.fetchall():
    print(row)

print("Клиент - товар:")
cursor.execute("""
    SELECT customers.name, orders.product
    FROM customers
    JOIN orders ON customers.id = orders.customer_id 
""")
for row in cursor.fetchall():
    print(row)

print("Заказы дороже 5000")
cursor.execute("""
    SELECT customers.name, orders.product, orders.price
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
    WHERE orders.price > 5000
""")
for row in cursor.fetchall():
    print(row)

print("Клиент - количество заказов:")
cursor.execute("""
    SELECT customers.name, COUNT(*)
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
    GROUP BY customers.id
""")
for row in cursor.fetchall():
    print(row)

print("Клиент - сумма - заказов:")
cursor.execute("""
    SELECT customers.name, SUM(orders.price)
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
    GROUP BY customers.id
""")
for row in cursor.fetchall():
    print(row)


print("Все заказы по убыванию")

cursor.execute("""
    SELECT customers.name, orders.product, orders.price
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
    ORDER BY orders.price DESC
""")
for row in cursor.fetchall():
    print(row)
conn.close()