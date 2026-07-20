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

    if not question.strip():
        st.warning("Escribe una pregunta.")
        st.stop()

    try:

        with st.spinner("🧠 Generando SQL..."):
            sql = generate_sql(question)

        st.subheader("📄 SQL generado")
        st.code(sql, language="sql")

        with st.spinner("📊 Consultando Supabase..."):
            df = execute_query(sql)

        st.subheader("📈 Resultado")
        st.dataframe(df, use_container_width=True)

        # =====================================
        # VISUALIZACIÓN AUTOMÁTICA
        # =====================================

        if len(df.columns) == 2:

            x = df.columns[0]
            y = df.columns[1]

            # Verifica que la segunda columna sea numérica
            if df[y].dtype.kind in "iuf":

                st.subheader("📊 Visualización")

                st.bar_chart(
                    df.set_index(x)
                )

    except Exception as e:

        st.error(f"Ocurrió un error:\n\n{e}")