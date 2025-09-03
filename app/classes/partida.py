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
        self.resultado = resultado
        self.pgn = pgn
        self.brancas = brancas
        self.pretas = pretas
        self.rodada = rodada