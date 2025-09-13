"""
Migration: Add players table
Created: Initial migration
"""
from app.db import db

def migrate():
    """Cria a tabela de jogadores"""
    db.create_table(
        'jogadores',
        {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'rating_id': 'INTEGER',
            'nome': 'TEXT NOT NULL',
            'federacao': 'TEXT NOT NULL',
            'data_nascimento': 'TEXT NOT NULL',
            'sexo': 'INTEGER NOT NULL',
            'FOREIGN KEY(rating_id)': 'REFERENCES ratings(id)'
        }
    )

def rollback():
    """Remove a tabela de jogadores"""
    from app.db import db
    db.execute("DROP TABLE IF EXISTS jogadores")