from batch.functions import get_files, read_csv_file
from src.schemas.data_types import batch_data_types
from db.queries import create_table, insert_historical_data, get_schema
import os

folder_path = os.path.join(os.getcwd(), 'data/raw')

def load_data():

    tables = ['departments', 'jobs', 'hired_employees']

    for table in tables:
        schema = get_schema(table)
        create_table(table, schema)

    files = get_files(folder_path)

    for file in files:
        df = read_csv_file(folder_path, file)
        for col_name, expected_type in batch_data_types[file].items():
            actual_type = df[col_name].dtype.type
            if actual_type != expected_type:
                df[col_name] = df[col_name].fillna(0).astype(expected_type)
        insert_historical_data(file.split('.')[0], df)