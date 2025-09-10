from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from app.utils.enums import ControleTempo
from .torneio import Torneio

if TYPE_CHECKING:
    from .rodada import Rodada
    from .participacao import Participacao

class TorneioEliminatorio(Torneio):
    def __init__(
        self, 
        nome: str, 
        local: str, 
        data: datetime, 
        controle_tempo: ControleTempo, 
        descricao: Optional[str] = None,
        jogadores: Optional[List["Participacao"]] = None,
        rodadas: Optional[List["Rodada"]] = None
    ):
        super().__init__(nome, local, data, controle_tempo, descricao, jogadores, rodadas)

    def emparceirar(self):
        print("Emparceiramento para torneio eliminatório ainda não implementado.")