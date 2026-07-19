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
    sql = sql.upper()
    return any(func in sql for func in SQLITE_FUNCTIONS)


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

    for _ in range(3):

        sql = ask_llm(
            SYSTEM_PROMPT,
            prompt
        ).strip()

        if not contains_sqlite(sql):
            return sql

        prompt += """

La consulta anterior fue incorrecta porque utilizó funciones de SQLite.

Reescribe completamente la consulta.

Está prohibido utilizar:

- STRFTIME
- PRAGMA
- sqlite_master
- julianday
- datetime()
- IFNULL

Utiliza únicamente PostgreSQL.

Para fechas usa:

- DATE_TRUNC()
- EXTRACT()
- TO_CHAR()

Devuelve únicamente SQL.
"""

    raise Exception(
        "No fue posible generar una consulta PostgreSQL válida."
    )