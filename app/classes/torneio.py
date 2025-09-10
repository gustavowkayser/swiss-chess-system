from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from app.utils.enums import ControleTempo
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from .participacao import Participacao
    from .rodada import Rodada

class Torneio(ABC):
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
        self.__nome = nome
        self.__local = local
        self.__data = data
        self.__controle_tempo = controle_tempo
        self.__jogadores = jogadores
        self.__descricao = descricao
        self.__rodadas = rodadas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, value):
        self.__local = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def organizador(self):
        return self.__organizador

    @organizador.setter
    def organizador(self, value):
        self.__organizador = value

    @property
    def controle_tempo(self):
        return self.__controle_tempo

    @controle_tempo.setter
    def controle_tempo(self, value):
        self.__controle_tempo = value

    @property
    def jogadores(self):
        return self.__jogadores

    @jogadores.setter
    def jogadores(self, value):
        self.__jogadores = value

    @property
    def rodadas(self):
        return self.__rodadas

    @rodadas.setter
    def rodadas(self, value):
        self.__rodadas = value

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @abstractmethod
    def emparceirar(self):
        raise NotImplementedError("O método emparceirar deve ser implementado nas subclasses.")