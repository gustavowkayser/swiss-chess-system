from ..db import db
from typing import Dict, Tuple
from app.logger import Logger, LogLevel
from app.dtos.rating_dto import RatingDTO

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
    
    def add_player(self, data: dict):
        try:
            rating = RatingDTO.to_dict(data['rating'])
            rating_id = db.insert("ratings", tuple(rating.keys()), tuple(rating.values()))
            new_data = {
                'nome': data['nome'],
                'federacao': data['federacao'],
                'data_nascimento': data['data_nascimento'],
                'sexo': data['sexo'],
                'rating_id': rating_id
            }
            db.insert("jogadores", tuple(new_data.keys()), tuple(new_data.values()))
        except Exception as e:
            self.logger.error("Erro ao adicionar jogador/rating", {"error": str(e), "data": data, "rating_id": rating_id, "rating": rating})
            return False
        return True
    
    def get_torneios(self) -> list:
        try:
            result = db.select_all("torneios")
        except Exception as e:
            self.logger.error(f"Erro ao buscar torneios: {e}")
            return []
        
        return result
    
    def get_jogadores(self) -> list:
        try:
            result = db.select_all("jogadores")
        except Exception as e:
            self.logger.error(f"Erro ao buscar jogadores: {e}")
            return []
        
        return result

db_repository = DBRepository()