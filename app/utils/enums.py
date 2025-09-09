from enum import Enum

class Resultado(Enum):
    BRANCAS_VENCEM = "1-0"
    EMPATE = "1/2-1/2"
    PRETAS_VENCEM = "0-1"

class Sexo(Enum):
    MASCULINO = "M"
    FEMININO = "F"

class ControleTempo(Enum):
    CLASSICO = "Clássico"
    RAPIDO = "Rápido"
    BLITZ = "Blitz"

class TipoDesempate(Enum):
    CONFRONTO_DIRETO = "Confronto Direto"
    BUCHHOLZ = "Buchholz"
    BUCHHOLZ_MEDIO = "Buchholz Médio"
    SONNENBORN_BERGER = "Sonnenborn-Berger"