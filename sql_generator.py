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

Genera únicamente SQL válido para SQLite.
"""

    sql = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    return sql.strip()