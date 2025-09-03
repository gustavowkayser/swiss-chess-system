from datetime import datetime
from typing import List, Optional
from app.classes import Partida, Torneio

class Rodada:
    def __init__(
        self,
        numero: int,
        data: datetime,
        torneio: Torneio,
        partidas: Optional[List[Partida]] = None,
    ):
        self.numero = numero
        self.data = data
        self.partidas = partidas
        self.torneio = torneio