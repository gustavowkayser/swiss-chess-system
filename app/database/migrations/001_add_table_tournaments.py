"""
Migration: Add tournaments table
Created: Initial migration
"""
from app.db import db

def migrate():
    """Cria a tabela de torneios"""
    db.create_table(
        'torneios',
        {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'descricao': 'TEXT',
            'controle_tempo': 'TEXT NOT NULL',
            'data': 'TEXT NOT NULL',
            'local': 'TEXT NOT NULL',
            'tipo': 'TEXT NOT NULL',
            'numero_rodadas': 'INTEGER'
        }
    )

def rollback():
    """Remove a tabela de torneios"""
    from app.db import db
    db.execute("DROP TABLE IF EXISTS torneios")