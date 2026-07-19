import os
import psycopg
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    DATABASE_URL = st.secrets["DATABASE_URL"]


def get_schema():

    with psycopg.connect(DATABASE_URL) as conn:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                table_name,
                column_name,
                data_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position;
        """)

        rows = cursor.fetchall()

    schema = ""

    current_table = None

    for table, column, data_type in rows:

        if table != current_table:
            schema += f"\n\nTABLA: {table}\n"
            current_table = table

        schema += f"- {column} ({data_type})\n"

    return schema