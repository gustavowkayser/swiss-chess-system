from app.classes import Torneio, Jogador, Partida
from typing import Optional, List

class Participacao(Jogador):
    def __init__(
        self, 
        federacao: str, 
        rating: float, 
        rating_acumulado: float, 
        jogador: Jogador,
        torneio: Torneio,
        pontos: Optional[float] = None, 
        desempates: Optional[float] = None,
        partidas: Optional[List[Partida]] = None
    ):
        super().__init__(
            nome=jogador.nome,
            federacao=jogador.federacao,
            data_nascimento=jogador.data_nascimento,
            sexo=jogador.sexo,
            rating=jogador.rating,
            partidas=partidas,
            participacoes=jogador.participacoes
        )
        self.federacao = federacao
        self.rating = rating
        self.rating_acumulado = rating_acumulado
        self.pontos = pontos
        self.desempates = desempates
        self.jogador = jogador
        self.torneio = torneio