from groq_client import ask_llm
from schema import get_schema
from prompts import SYSTEM_PROMPT


def generate_sql(question):

    schema = get_schema()

    prompt = f"""
Base de datos:

{schema}

Pregunta del usuario:

{question}

Genera únicamente SQL válido para PostgreSQL.

IMPORTANTE:

La base de datos es PostgreSQL.

Está prohibido utilizar funciones de SQLite.

NO utilices nunca:

- STRFTIME
- PRAGMA
- sqlite_master
- IFNULL
- AUTOINCREMENT
- julianday
- datetime()

Para trabajar con fechas utiliza únicamente:

- DATE_TRUNC()
- EXTRACT()
- TO_CHAR()

Reglas:

- Devuelve únicamente el SQL.
- No agregues explicaciones.
- No agregues texto antes o después del SQL.
- No uses Markdown.
- No escribas ```sql.
- Utiliza exclusivamente las tablas y columnas proporcionadas en el esquema.
- Nunca inventes tablas.
- Nunca inventes columnas.
- Usa JOIN cuando sea necesario.
- El SQL debe ejecutarse correctamente en PostgreSQL.
"""

    sql = ask_llm(
        SYSTEM_PROMPT,
        prompt
    ).strip()

    sqlite_functions = [
        "STRFTIME",
        "PRAGMA",
        "SQLITE_MASTER",
        "JULIANDAY",
        "IFNULL",
        "AUTOINCREMENT",
        "DATETIME("
    ]

    if any(func in sql.upper() for func in sqlite_functions):

        sql = ask_llm(
            SYSTEM_PROMPT,
            prompt + """

La consulta anterior utilizó funciones de SQLite.

Reescribe completamente la consulta utilizando únicamente sintaxis PostgreSQL.

Recuerda:

- No uses STRFTIME.
- No uses PRAGMA.
- No uses sqlite_master.
- Para fechas utiliza DATE_TRUNC(), EXTRACT() o TO_CHAR().
"""
        ).strip()

    return sql