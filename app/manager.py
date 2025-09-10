from . import logger
from .classes import TorneioSuico, TorneioEliminatorio
from .utils.enums import TipoTorneio, ControleTempo
from .request import Request
from datetime import date

class App:
    def __init__(self):
        self.logger = None
        self.functions_map = {
            "registrar-torneio": self.register_tournament,
        } 

    def execute(self, function, *args):
        self.logger = logger.Logger(log_level=logger.LogLevel.DEBUG if "--debug" in args else logger.LogLevel.DEFAULT)
        self.request = Request(self.logger)
        if function in self.functions_map:
            self.logger.debug(f"Executando a função '{function}' com os seguintes argumentos: {', '.join(str(arg) for arg in args)}")
            self.functions_map[function]()
        else:
            self.logger.error(f"Função '{function}' não reconhecida.", context={"function": function})

    def register_tournament(self):
        self.logger.info("Registrando torneio...")

        tipo = self.request.get_input(
            prompt="Torneio Suíço (1) ou Eliminatório (2): ", 
            expected_type=int, 
            choices=[TipoTorneio.SUICO.value, TipoTorneio.ELIMINATORIO.value])

        nome = self.request.get_input(
            prompt="Nome do torneio: ", 
            expected_type=str, 
            min_length=2, 
            max_length=100)
        local = self.request.get_input(
            prompt="Local do torneio: ", 
            expected_type=str, 
            min_length=2, 
            max_length=100)
        data = self.request.get_input(
            prompt="Data de início (DD/MM/AAAA): ", 
            expected_type=date)
        controle_tempo = self.request.get_input(
            prompt="Controle de tempo (Clássico [1], Rápido [2], Blitz [3]): ", 
            expected_type=int, 
            choices=[ControleTempo.CLASSICO.value, ControleTempo.RAPIDO.value, ControleTempo.BLITZ.value])
        if tipo == TipoTorneio.SUICO.value:
            numero_rodadas = self.request.get_input(
                prompt="Número de rodadas: ",
                expected_type=int,
                min_length=1)

        torneio = TorneioSuico(
            nome=nome,
            local=local,
            data=data,
            numero_rodadas=numero_rodadas,
            controle_tempo=controle_tempo
        ) if tipo == TipoTorneio.SUICO.value else TorneioEliminatorio(
            nome=nome,
            local=local,
            data=data,
            controle_tempo=controle_tempo
        )

        self.logger.info(f"Torneio '{torneio.nome}' registrado com sucesso!")
