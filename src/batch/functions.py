from src.schemas.data_types import batch_data_types
import os
import pandas as pd

def get_files(path):
    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    return csv_files

def read_csv_file(path, csv_file):

    file_path = os.path.join(path, csv_file)
    df = pd.read_csv(file_path, header=None, dtype=batch_data_types[csv_file])
    column_names = list(batch_data_types[csv_file].keys())
    df.columns = column_names
    df = df.reset_index(drop=True)

    return df

