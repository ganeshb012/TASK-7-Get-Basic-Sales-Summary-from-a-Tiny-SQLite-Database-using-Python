import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        product TEXT,
        quantity INTEGER,
        price INTEGER
    )
""")

data = [
    ('Apple', 10, 5),
    ('Banana', 15, 2),
    ('Apple', 5, 5),
    ('Banana', 10, 2),
    ('Orange', 8, 3)
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()

print("✅ Database created with sample data!")

