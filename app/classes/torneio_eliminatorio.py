from datetime import datetime
from typing import List, Optional
from app.classes import Torneio, Rodada, Participacao
from app.utils.enums import ControleTempo

class TorneioEliminatorio(Torneio):
    def __init__(
        self, 
        nome: str, 
        local: str, 
        data: datetime, 
        controle_tempo: ControleTempo, 
        descricao: Optional[str] = None,
        jogadores: Optional[List[Participacao]] = None,
        rodadas: Optional[List[Rodada]] = None
    ):
        super().__init__(nome, local, data, controle_tempo, descricao, jogadores, rodadas)