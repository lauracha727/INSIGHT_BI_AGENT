from database import execute_query

df = execute_query("""
SELECT *
FROM customers
LIMIT 5
""")

print(df)