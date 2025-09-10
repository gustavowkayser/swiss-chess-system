from . import logger

class App:
    def __init__(self):
        self.logger = None
        self.functions_map = {
            "registrar-torneio": self.register_tournament,
        } 

    def execute(self, function, *args):
        self.logger = logger.Logger(log_level=logger.LogLevel.DEBUG if "--debug" in args else logger.LogLevel.DEFAULT)
        if function in self.functions_map:
            self.logger.debug(f"Executando a função '{function}' com os seguintes argumentos: {', '.join(str(arg) for arg in args)}")
            self.functions_map[function]()
        else:
            self.logger.error(f"Função '{function}' não reconhecida.", context={"function": function})

    def register_tournament(self):
        self.logger.info("Registrando torneio...")