from ..db import db
from typing import Dict, Tuple

class DBRepository:
    """Repositório para operações de banco de dados."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DBRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def create_table(self, table_name: str, schema: Dict[str, str]):
        import re
        # Only allow alphanumeric and underscores for table and column names
        if not re.match(r'^\w+$', table_name):
            raise ValueError("Invalid table name")
        valid_types = {'INTEGER', 'TEXT', 'REAL', 'BLOB', 'NUMERIC'}
        columns = []
        for name, dtype in schema.items():
            if not re.match(r'^\w+$', name):
                raise ValueError(f"Invalid column name: {name}")
            if dtype.upper() not in valid_types:
                raise ValueError(f"Invalid SQL type: {dtype}")
            columns.append(f"{name} {dtype.upper()}")
        columns_str = ', '.join(columns)
        # Validate table name again before executing
        if not re.match(r'^\w+$', table_name):
            raise ValueError("Invalid table name")
        query = f"CREATE TABLE IF NOT EXISTS \"{table_name}\" ({columns_str})"
        db.execute(query)

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
        db.execute(query, values)

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
        db.execute(query, params)
        result = db.fetchall()
        return result[0][0] if result else 0

db_repository = DBRepository()