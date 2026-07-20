from groq_client import ask_llm
from schema import get_schema
from prompts import SYSTEM_PROMPT


SQLITE_FUNCTIONS = [
    "STRFTIME",
    "PRAGMA",
    "SQLITE_MASTER",
    "JULIANDAY",
    "IFNULL",
    "AUTOINCREMENT",
    "DATETIME("
]


def contains_sqlite(sql):
    sql_upper = sql.upper()
    return any(func in sql_upper for func in SQLITE_FUNCTIONS)


def generate_sql(question):

    schema = get_schema()

    prompt = f"""
Base de datos:

{schema}

Pregunta del usuario:

{question}

Genera únicamente SQL válido para PostgreSQL.

IMPORTANTE:

- La base de datos es PostgreSQL.
- Nunca utilices funciones de SQLite.
- Para fechas utiliza únicamente:
    - DATE_TRUNC()
    - EXTRACT()
    - TO_CHAR()

Reglas:

- Devuelve únicamente SQL.
- No agregues explicaciones.
- No uses Markdown.
- No escribas ```sql.
- Utiliza únicamente las tablas y columnas del esquema.
"""

    for intento in range(3):

        sql = ask_llm(
            SYSTEM_PROMPT,
            prompt
        ).strip()

        print("=" * 80)
        print(f"Intento {intento + 1}")
        print("SQL generado:")
        print(repr(sql))
        print("contains_sqlite =", contains_sqlite(sql))
        print("=" * 80)

        if not contains_sqlite(sql):
            return sql

        prompt += f"""

La consulta anterior fue incorrecta porque utilizó funciones de SQLite.

SQL generado:

{sql}

Reescribe completamente la consulta.

Está prohibido utilizar:

- STRFTIME
- PRAGMA
- SQLITE_MASTER
- JULIANDAY
- IFNULL
- AUTOINCREMENT
- DATETIME()

Recuerda:

- La base de datos es PostgreSQL.
- Usa únicamente:
    - EXTRACT()
    - DATE_TRUNC()
    - TO_CHAR()

Devuelve únicamente SQL válido para PostgreSQL.
"""

    raise Exception(
        f"""El modelo generó SQL de SQLite en los 3 intentos.

Último SQL generado:

{sql}
"""
    )