from app.classes import Jogador

class JogadorDTO:
    def __init__(self):
        pass

    @staticmethod
    def to_dict(jogador: Jogador) -> dict:
        return {
            'nome': jogador.nome,
            'federacao': jogador.federacao,
            'data_nascimento': jogador.data_nascimento,
            'sexo': jogador.sexo,
            'rating': jogador.rating
        }
