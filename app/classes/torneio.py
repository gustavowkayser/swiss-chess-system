from datetime import datetime
from typing import List, Optional
from app.classes import Jogador, Rodada
from app.utils.enums import ControleTempo

class Torneio:
    def __init__(
        self, 
        nome: str, 
        local: str, 
        data: datetime, 
        organizador: str, 
        controle_tempo: ControleTempo, 
        descricao: Optional[str] = None,
        jogadores: Optional[List[Jogador]] = None, 
        rodadas: Optional[List[Rodada]] = None
    ):
        self.nome = nome
        self.local = local
        self.data = data
        self.organizador = organizador
        self.controle_tempo = controle_tempo
        self.jogadores = jogadores
        self.rodadas = rodadas
        self.descricao = descricao