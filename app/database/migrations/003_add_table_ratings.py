"""
Migration: Add ratings table
Created: Initial migration
"""
from app.db import db

def migrate():
    """Cria a tabela de ratings"""
    db.create_table(
        'ratings',
        {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'rating_classico': 'INTEGER',
            'rating_rapido': 'INTEGER',
            'rating_blitz': 'INTEGER',
        }
    )

def rollback():
    """Remove a tabela de ratings"""
    from app.db import db
    db.execute("DROP TABLE IF EXISTS ratings")