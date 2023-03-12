import sqlite3

def get_db_connection():
    db_connection = sqlite3.connect('globant.db')
    return db_connection