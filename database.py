import sqlite3
import pandas as pd

DATABASE = "database/olist.sqlite"


def get_connection():
    return sqlite3.connect(DATABASE)


def execute_query(sql):
    conn = get_connection()
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df