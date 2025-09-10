from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from app.utils.enums import ControleTempo
from .torneio import Torneio

if TYPE_CHECKING:
    from .rodada import Rodada
    from .participacao import Participacao

class TorneioSuico(Torneio):
    def __init__(
        self, 
        nome: str, 
        local: str, 
        data: datetime,
        numero_rodadas: int,
        controle_tempo: ControleTempo, 
        descricao: Optional[str] = None,
        jogadores: Optional[List["Participacao"]] = None,
        rodadas: Optional[List["Rodada"]] = None
    ):
        super().__init__(nome, local, data, controle_tempo, descricao, jogadores, rodadas)
        self.__numero_rodadas = numero_rodadas

    @property
    def numero_rodadas(self):
        return self.__numero_rodadas

    @numero_rodadas.setter
    def numero_rodadas(self, value):
        self.__numero_rodadas = value

    def emparceirar(self):
        print("Emparceiramento para torneio suíço ainda não implementado.")