from enum import Enum

class TipoTorneio(Enum):
    SUICO = 1
    ELIMINATORIO = 2

class Resultado(Enum):
    BRANCAS_VENCEM = "1-0"
    EMPATE = "1/2-1/2"
    PRETAS_VENCEM = "0-1"

class Sexo(Enum):
    MASCULINO = "M"
    FEMININO = "F"

class ControleTempo(Enum):
    CLASSICO = 1
    RAPIDO = 2
    BLITZ = 3

class TipoDesempate(Enum):
    CONFRONTO_DIRETO = 1
    BUCHHOLZ = 2
    BUCHHOLZ_MEDIO = 3
    SONNENBORN_BERGER = 4