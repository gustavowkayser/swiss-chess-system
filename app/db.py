import sqlite3
import os

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

db = DB()
