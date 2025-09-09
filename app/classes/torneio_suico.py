from app.classes import Torneio, Rodada, Participacao
from typing import Optional, List
from datetime import datetime
from app.utils.enums import ControleTempo

class TorneioSuico(Torneio):
    def __init__(
        self, 
        nome: str, 
        local: str, 
        data: datetime,
        numero_rodadas: int,
        controle_tempo: ControleTempo, 
        descricao: Optional[str] = None,
        jogadores: Optional[List[Participacao]] = None,
        rodadas: Optional[List[Rodada]] = None
    ):
        super().__init__(nome, local, data, controle_tempo, descricao, jogadores, rodadas)
        self.__numero_rodadas = numero_rodadas

    @property
    def numero_rodadas(self):
        return self.__numero_rodadas

    @numero_rodadas.setter
    def numero_rodadas(self, value):
        self.__numero_rodadas = value