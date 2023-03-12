from db.connection import get_db_connection
import json

def create_table(table_name, schema):
    conn = get_db_connection()
    cursor = conn.cursor()

    column_defs = ", ".join([f"{column_name} {column_type}" for column_name, column_type in schema.items()])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})")

def insert_historical_data(table_name, df):
    conn = get_db_connection()
    df.to_sql(table_name, conn, if_exists='replace', index=False)

def get_schema(table_name):
    with open(f'src/schemas/{table_name}.json') as f:
        schema = json.load(f)
    return schema