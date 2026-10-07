import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT
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

cursor.execute("INSERT INTO customers (name) VALUES (?)", ("Иван",))
cursor.execute("INSERT INTO customers (name) VALUES (?)", ("Мария",))
cursor.execute("INSERT INTO customers (name) VALUES (?)", ("Пётр",))
cursor.execute("INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)", (1, "Ноутбук", 50000))
cursor.execute("INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)", (1, "Мышь", 1500))
cursor.execute("INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)", (2, "Клавиатура", 3000))
conn.commit()

print("Имя клиента и товар:")
cursor.execute("""
    SELECT customers.name, orders.product
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
""")
for row in cursor.fetchall():
    print(row)

print("\nКоличесвто закзаов у каждого клиента:")
cursor.execute("""
    SELECT customers.name, COUNT(*)
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
    GROUP BY customers.id
""")
for row in cursor.fetchall():
    print(row)

print("\nСумма заказов покупателей:")
cursor.execute("""
SELECT customers.name, SUM(orders.price)
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id
""")
for row in cursor.fetchall():
    print(row)
    
conn.close()