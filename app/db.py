import sqlite3
import os
from typing import Dict, Tuple, List, Any

class DB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_name="swiss-chess-system.db"):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        self.connection = sqlite3.connect(f'{os.path.dirname(__file__)}/database/{db_name}')
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()

    def select(self, values: List[str], table: str) -> List[Any]:
        query = f'SELECT ({values}) FROM {table}'
        self.execute(query)
        result = self.fetchall()
        return result[0][0] if result else None
    
    def select_all(self, table: str) -> List[Any]:
        query = f'SELECT * FROM {table}'
        self.execute(query)
        result = self.fetchall()
        return result if result else None

    def create_table(self, table_name: str, schema: Dict[str, str]):
        import re
        # Only allow alphanumeric and underscores for table and column names
        if not re.match(r'^\w+$', table_name):
            raise ValueError("Invalid table name")
        columns = []
        for name, dtype in schema.items():
            if not re.match(r'^\w+$', name):
                raise ValueError(f"Invalid column name: {name}")
            columns.append(f"{name} {dtype.upper()}")
        columns_str = ', '.join(columns)
        # Validate table name again before executing
        if not re.match(r'^\w+$', table_name):
            raise ValueError("Invalid table name")
        query = f"CREATE TABLE IF NOT EXISTS \"{table_name}\" ({columns_str})"
        self.execute(query)

    def insert(self, table_name: str, columns: Tuple[str], values: Tuple[str]):
        import re
        # Validate table and column names
        if not re.match(r'^\w+$', table_name):
            raise ValueError("Invalid table name")
        for col in columns:
            if not re.match(r'^\w+$', col):
                raise ValueError(f"Invalid column name: {col}")
        placeholders = ', '.join(['?' for _ in values])
        columns_str = ', '.join([f'"{col}"' for col in columns])
        query = f'INSERT INTO "{table_name}" ({columns_str}) VALUES ({placeholders})'
        self.execute(query, values)

    def count(self, table_name: str, where_clause: str = "") -> int:
        import re
        # Validate table name
        if not re.match(r'^\w+$', table_name):
            raise ValueError("Invalid table name")
        query = f'SELECT COUNT(*) FROM "{table_name}"'
        params = ()
        if where_clause:
            # Optionally, you could parse and validate the where_clause more strictly
            query += f" WHERE {where_clause}"
        self.execute(query, params)
        result = self.fetchall()
        return result[0][0] if result else 0

db = DB()
