from groq_client import ask_llm


SYSTEM_ANALYST = """
Eres un analista senior de Business Intelligence.

Tu trabajo es interpretar resultados obtenidos de consultas SQL.

Reglas:

- Habla en español.
- Máximo 4 líneas.
- No inventes datos.
- Basa tu análisis únicamente en la información entregada.
- Si el resultado tiene una sola fila, explica qué significa.
- Si hay varias filas, destaca tendencias o diferencias importantes.
- No repitas la tabla.
"""


def explain_result(question, df):

    prompt = f"""
Pregunta del usuario:

{question}

Resultado de la consulta:

{df.to_markdown(index=False)}

Genera una interpretación ejecutiva.
"""

    return ask_llm(
        SYSTEM_ANALYST,
        prompt
    )