from ..db import db
from typing import Dict, Tuple
from app.logger import Logger, LogLevel

class DBRepository:
    """Repositório para operações de banco de dados."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DBRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self, logger: Logger = Logger(LogLevel.DEFAULT)):
        self.logger = logger
    
    def add_torneio(self, data: dict):
        try:
            db.insert("torneios", tuple(data.keys()), tuple(data.values()))
        except Exception as e:
            self.logger.error("Erro ao adicionar torneio", {"error": str(e), "data": data})
            return False
        return True
    
    def get_torneios(self) -> list:
        try:
            result = db.select_all("torneios")
        except Exception as e:
            self.logger.error(f"Erro ao buscar torneios: {e}")
            return []
        
        return result

db_repository = DBRepository()