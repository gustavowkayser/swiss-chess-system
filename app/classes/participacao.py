from app.classes import Torneio, Jogador, Partida, Rating, Desempate
from typing import Optional, List

class Participacao:
    def __init__(
        self, 
        federacao: str, 
        rating: Rating, 
        jogador: Jogador,
        torneio: Torneio,
        pontos: Optional[float] = None, 
        desempates: Optional[List[Desempate]] = None,
        partidas: Optional[List[Partida]] = None
    ):
        self.__federacao = federacao
        self.__rating = rating
        self.__pontos = pontos
        self.__desempates = desempates
        self.__jogador = jogador
        self.__torneio = torneio
        self.__desempates = desempates
        self.__partidas = partidas

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

    @property
    def partidas(self):
        return self.__partidas
    
    @partidas.setter
    def partidas(self, value):
        self.__partidas = value