import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the database
conn = sqlite3.connect("sales_data.db")

# Step 2: Write SQL query
query = """
SELECT product, 
       SUM(quantity) AS total_quantity,
       SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

# Step 3: Read data into DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Print results
print("📊 Sales Summary:")
print(df)

# Step 5: Plot bar chart for revenue
df.plot(kind='bar', x='product', y='total_revenue', legend=False)
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional: Save chart
plt.show()

# Step 6: Close connection
conn.close()
