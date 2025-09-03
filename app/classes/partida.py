from app.classes import Jogador, Rodada
from app.utils.enums import Resultado

class Partida:
    def __init__(
        self,
        resultado: Resultado,
        pgn: str,
        brancas: Jogador,
        pretas: Jogador,
        rodada: Rodada,
    ):
        self.__resultado = resultado
        self.__pgn = pgn
        self.__brancas = brancas
        self.__pretas = pretas
        self.__rodada = rodada

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, value):
        self.__resultado = value

    @property
    def pgn(self):
        return self.__pgn

    @pgn.setter
    def pgn(self, value):
        self.__pgn = value

    @property
    def brancas(self):
        return self.__brancas

    @brancas.setter
    def brancas(self, value):
        self.__brancas = value

    @property
    def pretas(self):
        return self.__pretas

    @pretas.setter
    def pretas(self, value):
        self.__pretas = value

    @property
    def rodada(self):
        return self.__rodada

    @rodada.setter
    def rodada(self, value):
        self.__rodada = value