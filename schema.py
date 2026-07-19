import sqlite3

DATABASE = "database/olist.sqlite"


def get_schema():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
    """)

    tables = [row[0] for row in cursor.fetchall()]

    schema = ""

    for table in tables:

        schema += f"\n\nTABLA: {table}\n"

        cursor.execute(f"PRAGMA table_info('{table}')")

        columns = cursor.fetchall()

        for column in columns:
            schema += f"- {column[1]} ({column[2]})\n"

    conn.close()

    return schema