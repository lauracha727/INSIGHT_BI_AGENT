from sql_generator import generate_sql
from database import execute_query

question = "¿Cuáles fueron las 10 ciudades con más ventas?"

sql = generate_sql(question)

print("\nSQL generado:\n")
print(sql)

print("\nResultado:\n")

df = execute_query(sql)

print(df)