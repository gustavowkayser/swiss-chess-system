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
        self.__federacao = federacao
        self.__rating = rating
        self.__rating_acumulado = rating_acumulado
        self.__pontos = pontos
        self.__desempates = desempates
        self.__jogador = jogador
        self.__torneio = torneio

    @property
    def federacao(self):
        return self.__federacao

    @federacao.setter
    def federacao(self, value):
        self.__federacao = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def rating_acumulado(self):
        return self.__rating_acumulado

    @rating_acumulado.setter
    def rating_acumulado(self, value):
        self.__rating_acumulado = value

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, value):
        self.__pontos = value

    @property
    def desempates(self):
        return self.__desempates

    @desempates.setter
    def desempates(self, value):
        self.__desempates = value

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, value):
        self.__jogador = value

    @property
    def torneio(self):
        return self.__torneio

    @torneio.setter
    def torneio(self, value):
        self.__torneio = value