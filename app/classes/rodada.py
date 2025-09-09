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
        subrodada: Optional[int] = None
    ):
        self.__numero = numero
        self.__data = data
        self.__partidas = partidas
        self.__torneio = torneio
        self.__subrodada = subrodada

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def partidas(self):
        return self.__partidas

    @partidas.setter
    def partidas(self, value):
        self.__partidas = value

    @property
    def torneio(self):
        return self.__torneio

    @torneio.setter
    def torneio(self, value):
        self.__torneio = value

    @property
    def subrodada(self):
        return self.__subrodada
    
    @subrodada.setter
    def subrodada(self, value):   
        self.__subrodada = value