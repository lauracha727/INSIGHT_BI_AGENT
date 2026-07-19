import streamlit as st

from sql_generator import generate_sql
from database import execute_query

st.set_page_config(
    page_title="INSIGHT BI AGENT",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 INSIGHT BI AGENT")

st.caption("Consulta tu base de datos utilizando lenguaje natural.")

question = st.text_input(
    "Pregunta",
    placeholder="Ej: ¿Cuáles fueron las 10 ciudades con más ventas?"
)

if st.button("Consultar"):

    if question.strip() == "":
        st.warning("Escribe una pregunta.")
        st.stop()

    with st.spinner("Generando SQL..."):

        sql = generate_sql(question)

    st.subheader("📄 SQL generado")

    st.code(sql, language="sql")

    with st.spinner("Consultando la base de datos..."):

        df = execute_query(sql)

    st.subheader("📊 Resultado")

    st.dataframe(df, use_container_width=True)