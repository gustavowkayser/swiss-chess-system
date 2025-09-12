from app.classes import Torneio, TorneioSuico, TorneioEliminatorio

class TorneioSuicoDTO:
    def __init__(self):
        pass

    @staticmethod
    def to_dict(torneio: TorneioSuico) -> dict:
        return {
            'nome': torneio.nome,
            'descricao': torneio.descricao,
            'controle_tempo': torneio.controle_tempo,
            'data': torneio.data,
            'local': torneio.local,
            'tipo': 1,
            'numero_rodadas': torneio.numero_rodadas
        }
    
class TorneioEliminatorioDTO:
    def __init__(self):
        pass

    @staticmethod
    def to_dict(torneio: TorneioEliminatorio) -> dict:
        return {
            'nome': torneio.nome,
            'descricao': torneio.descricao,
            'controle_tempo': torneio.controle_tempo,
            'data': torneio.data,
            'local': torneio.local,
            'tipo': 1,
        }