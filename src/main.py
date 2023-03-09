import os
import pandas as pd

data_types = {
        'hired_employees.csv': {
            'id': int,
            'name': str,
            'datetime': str,
            'department_id': int,
            'job_id': int
        },
        'departments.csv': {
            'id': int,
            'department': str
        },
        'jobs.csv': {
            'id': int,
            'job': str
        }
    }

folder_path = os.path.join(os.getcwd(), 'docs/Challenge_DA')

def main():
    files = get_files(folder_path)

    for file in files:
        df = read_csv_file(folder_path, file)
        for col_name, expected_type in data_types[file].items():
            actual_type = df[col_name].dtype.type
            if actual_type != expected_type:
                df[col_name] = df[col_name].fillna(0).astype(expected_type)
        print(df)

def get_files(path):
    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    return csv_files

def read_csv_file(path, csv_file):

    file_path = os.path.join(path, csv_file)
    df = pd.read_csv(file_path, header=None, dtype=data_types[csv_file])
    column_names = list(data_types[csv_file].keys())
    df.columns = column_names
    df = df.reset_index(drop=True)

    return df