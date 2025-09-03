from datetime import date
from app.utils.enums import Sexo
from app.classes import Partida, Participacao, Rating
from typing import List, Optional

class Jogador:
    def __init__(self, 
        nome: str, 
        federacao: str, 
        data_nascimento: date,
        sexo: Sexo,
        rating: Rating,
        partidas: Optional[List[Partida]] = None,
        participacoes: Optional[List[Participacao]] = None
    ):
        self.nome = nome
        self.federacao = federacao
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.rating = rating
        self.partidas = partidas
        self.participacoes = participacoes