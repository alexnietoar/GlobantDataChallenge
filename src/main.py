from batch.ingest import load_data
from api.api import execute

def main():
    load_data()
    execute()