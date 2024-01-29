import sqlite3

class DataPersistence:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ', '.join(f'{name} {type}' for name, type in columns.items())
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});')

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))
        self.cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders});', tuple(data.values()))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()   
