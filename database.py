import pandas as pd
import psycopg
import streamlit as st

DATABASE_URL = st.secrets["DATABASE_URL"]


def execute_query(sql):
    with psycopg.connect(DATABASE_URL) as conn:
        return pd.read_sql_query(sql, conn)