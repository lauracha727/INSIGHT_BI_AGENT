import os
import pandas as pd
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def execute_query(sql):
    with psycopg.connect(DATABASE_URL) as conn:
        return pd.read_sql_query(sql, conn)