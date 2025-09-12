from . import logger
from .classes import TorneioSuico, TorneioEliminatorio
from .utils.enums import TipoTorneio, ControleTempo
from .request import Request
from .migration_manager import migration_manager
from datetime import date
from app.repositories.db_repository import db_repository
from app.dtos.torneio_dto import TorneioSuicoDTO, TorneioEliminatorioDTO

class App:
    def __init__(self):
        self.logger = None
        self.functions_map = {
            "migrate": self.migrate,
            "migration:create": self.create_migration,
            "migration:status": self.migration_status,
            "registrar-torneio": self.register_tournament,
            "registrar-torneio-exemplo": self.register_example_tournament,
            "listar-torneios": self.get_tournaments,
        } 

    def execute(self, function, *args):
        self.logger = logger.Logger(log_level=logger.LogLevel.DEBUG if "--debug" in args else logger.LogLevel.DEFAULT)

        self.request = Request(self.logger)
        if function in self.functions_map:
            self.logger.debug(f"Executando a função '{function}' com os seguintes argumentos: {', '.join(str(arg) for arg in args)}")
            self.functions_map[function]()
        else:
            self.logger.error(f"Função '{function}' não reconhecida.", context={"function": function})

    def migrate(self):
        """Executa todas as migrations pendentes"""
        self.logger.info("Iniciando processo de migração do banco de dados...")
        
        # Define o logger no migration manager
        migration_manager.set_logger(self.logger)
        
        # Executa as migrations
        success = migration_manager.run_migrations()
        
        if success:
            self.logger.info("Migração concluída com sucesso.")
        else:
            self.logger.error("Erro durante a migração do banco de dados.")

    def create_migration(self):
        """Cria uma nova migration"""
        self.logger.info("Criando nova migration...")
        
        name = self.request.get_input(
            prompt="Nome da migration: ", 
            expected_type=str, 
            min_length=3, 
            max_length=100)
        
        migration_manager.set_logger(self.logger)
        filename = migration_manager.create_migration(name)
        
        self.logger.info(f"Migration criada com sucesso: {filename}")
        self.logger.info(f"Edite o arquivo em: app/database/migrations/{filename}")

    def migration_status(self):
        """Mostra o status de todas as migrations"""
        self.logger.info("Verificando status das migrations...")
        
        migration_manager.set_logger(self.logger)
        status_list = migration_manager.get_migration_status()
        
        if not status_list:
            self.logger.info("Nenhuma migration encontrada.")
            return
        
        self.logger.info("Status das migrations:")
        for migration in status_list:
            status = "✓ EXECUTADA" if migration['executed'] else "✗ PENDENTE"
            self.logger.info(f"  {migration['number']:03d} - {migration['filename']} - {status}")

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

        try:
            db_repository.add_torneio(TorneioSuicoDTO.to_dict(torneio) if tipo == TipoTorneio.SUICO.value else TorneioEliminatorioDTO.to_dict(torneio))
        except Exception as e:
            self.logger.error(f"Erro ao registrar torneio: {e}")
            return
        self.logger.info(f"Torneio '{torneio.nome}' registrado com sucesso!")

    def register_example_tournament(self):
        torneio = TorneioSuico(
            nome="Caioba Chess Open 2025",
            local="Matinhos PR",
            data="10/10/2025",
            numero_rodadas=9,
            controle_tempo=ControleTempo.CLASSICO.value,
            descricao="Torneio anual na praia de Caiobá"
        )

        try:
            db_repository.add_torneio(TorneioSuicoDTO.to_dict(torneio))
        except Exception as e:
            self.logger.error(f"Erro ao registrar torneio: {e}")
            return
        self.logger.info(f"Torneio '{torneio.nome}' registrado com sucesso!")

    def get_tournaments(self):
        self.logger.info("Buscando torneios...")
        torneios = db_repository.get_torneios()
        if not torneios:
            self.logger.info("Nenhum torneio encontrado.")
            return
        for torneio in torneios:
            self.logger.info(f"  ID: {torneio[0]}, Nome: {torneio[1]}, Local: {torneio[2]}, Data: {torneio[3]}, Rodadas: {torneio[4]}, Controle de Tempo: {torneio[5]}")