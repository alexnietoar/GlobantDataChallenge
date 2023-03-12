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

def get_task1():
    query = open(f'src/db/sqls/task1.sql', encoding="UTF-8").read()
    results = execute_sql(query)

    json_results = []
    for row in results:
        json_results.append({
            'department': row[0],
            'job': row[1],
            'Q1': row[2],
            'Q2': row[3],
            'Q3': row[4],
            'Q4': row[5]
        })

    return json_results

def get_task2():
    query = open(f'src/db/sqls/task2.sql', encoding="UTF-8").read()
    results = execute_sql(query)

    json_results = []
    for row in results:
        json_results.append({
            'id': row[0],
            'department': row[1],
            'num_hires': row[2]
        })

    return json_results

def execute_sql(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()