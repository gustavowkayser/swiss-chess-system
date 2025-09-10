from datetime import date
from typing import List, Optional, TYPE_CHECKING
from app.utils.enums import Sexo

if TYPE_CHECKING:
    from .partida import Partida
    from .participacao import Participacao
    from .rating import Rating

class Jogador:
    def __init__(
        self, 
        nome: str, 
        federacao: str, 
        data_nascimento: date,
        sexo: Sexo,
        rating: "Rating",
        partidas: Optional[List["Partida"]] = None,
        participacoes: Optional[List["Participacao"]] = None
    ):
        self.__nome = nome
        self.__federacao = federacao
        self.__data_nascimento = data_nascimento
        self.__sexo = sexo
        self.__rating = rating
        self.__partidas = partidas
        self.__participacoes = participacoes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def federacao(self):
        return self.__federacao

    @federacao.setter
    def federacao(self, value):
        self.__federacao = value

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self.__data_nascimento = value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, value):
        self.__sexo = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def partidas(self):
        return self.__partidas

    @partidas.setter
    def partidas(self, value):
        self.__partidas = value

    @property
    def participacoes(self):
        return self.__participacoes

    @participacoes.setter
    def participacoes(self, value):
        self.__participacoes = value