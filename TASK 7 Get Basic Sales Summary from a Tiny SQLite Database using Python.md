# Sales Summary from SQLite using Python

## Task Overview
This project connects to a small SQLite database containing sales data and performs basic analysis using SQL inside Python.

## What It Does
- Connects to `sales_data.db` database
- Runs SQL queries to get total quantity sold and total revenue by product
- Displays the result in a table using pandas
- Plots a bar chart using matplotlib

## Files
- `create_sales_db.py`: Creates and populates the SQLite database with sample data
- `analyze_sales_data.py`: Analyzes and visualizes the data
- `sales_chart.png`: Bar chart showing revenue by product

## Output Example
| Product | Total Quantity | Total Revenue |
|---------|----------------|---------------|
| Apple   | 30             | 150           |
| Banana  | 50             | 100           |
| Orange  | 16             | 48            |

## Tools Used
- Python (sqlite3, pandas, matplotlib)
- SQLite (built-in)

