import os
import importlib.util
import re
from pathlib import Path
from typing import List, Tuple
from .db import db

class MigrationManager:
    """
    Gerenciador de migrations escalável que executa automaticamente
    todas as migrations na pasta de migrations em ordem.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        self.migrations_dir = os.path.join(os.path.dirname(__file__), 'database', 'migrations')
        self.logger = None
        self._ensure_migrations_table()
    
    def set_logger(self, logger):
        """Define o logger para usar durante as migrations"""
        self.logger = logger
    
    def _ensure_migrations_table(self):
        """Cria a tabela de controle de migrations se não existir"""
        db.create_table('migrations', {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'filename': 'TEXT NOT NULL UNIQUE',
            'executed_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
        })
    
    def _get_migration_files(self) -> List[Tuple[str, str]]:
        """
        Retorna lista de arquivos de migration ordenados pelo número.
        Retorna tuplas (numero, filename)
        """
        migration_files = []
        
        if not os.path.exists(self.migrations_dir):
            return migration_files
        
        for filename in os.listdir(self.migrations_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                # Extrai o número da migration do nome do arquivo
                match = re.match(r'^(\d+)_.*\.py$', filename)
                if match:
                    number = int(match.group(1))
                    migration_files.append((number, filename))
        
        # Ordena por número
        migration_files.sort(key=lambda x: x[0])
        return migration_files
    
    def _is_migration_executed(self, filename: str) -> bool:
        """Verifica se uma migration já foi executada"""
        result = db.count("migrations", f"filename = '{filename}'")
        return result > 0
    
    def _mark_migration_executed(self, filename: str):
        """Marca uma migration como executada"""
        db.insert("migrations", ("filename",), (filename,))
    
    def _load_migration_module(self, filename: str):
        """Carrega o módulo da migration"""
        migration_path = os.path.join(self.migrations_dir, filename)
        spec = importlib.util.spec_from_file_location(filename[:-3], migration_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    
    def _log(self, level: str, message: str):
        """Helper para logging"""
        if self.logger:
            getattr(self.logger, level, self.logger.info)(message)
        else:
            print(f"[{level.upper()}] {message}")
    
    def run_migrations(self) -> bool:
        """
        Executa todas as migrations pendentes em ordem.
        Retorna True se todas foram executadas com sucesso.
        """
        migration_files = self._get_migration_files()
        
        if not migration_files:
            self._log('info', 'Nenhuma migration encontrada.')
            return True
        
        self._log('info', f'Encontradas {len(migration_files)} migration(s).')
        
        executed_count = 0
        
        for number, filename in migration_files:
            if self._is_migration_executed(filename):
                self._log('debug', f'Migration {filename} já executada, pulando...')
                continue
            
            try:
                self._log('info', f'Executando migration: {filename}')
                
                # Carrega e executa a migration
                migration_module = self._load_migration_module(filename)
                
                if hasattr(migration_module, 'migrate'):
                    migration_module.migrate()
                    self._mark_migration_executed(filename)
                    executed_count += 1
                    self._log('info', f'Migration {filename} executada com sucesso.')
                else:
                    self._log('error', f'Migration {filename} não possui função migrate().')
                    return False
                    
            except Exception as e:
                self._log('error', f'Erro ao executar migration {filename}: {str(e)}')
                return False
        
        if executed_count == 0:
            self._log('info', 'Todas as migrations já estão atualizadas.')
        else:
            self._log('info', f'{executed_count} migration(s) executada(s) com sucesso.')
        
        return True
    
    def get_migration_status(self) -> List[dict]:
        """
        Retorna o status de todas as migrations.
        """
        migration_files = self._get_migration_files()
        status = []
        
        for number, filename in migration_files:
            is_executed = self._is_migration_executed(filename)
            status.append({
                'number': number,
                'filename': filename,
                'executed': is_executed
            })
        
        return status
    
    def create_migration(self, name: str) -> str:
        """
        Cria um novo arquivo de migration com template básico.
        Retorna o nome do arquivo criado.
        """
        # Determina o próximo número
        migration_files = self._get_migration_files()
        next_number = 1
        if migration_files:
            next_number = migration_files[-1][0] + 1
        
        # Sanitiza o nome
        clean_name = re.sub(r'[^a-zA-Z0-9_]', '_', name.lower())
        filename = f"{next_number:03d}_{clean_name}.py"
        filepath = os.path.join(self.migrations_dir, filename)
        
        # Template básico
        template = '''"""
Migration: {name}
Created: {date}
"""

def migrate():
    """
    Implementar a migration aqui.
    Exemplo:
    
    from app.db import db
    
    db.create_table(
        'table_name',
        {{
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'name': 'TEXT NOT NULL',
            'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
        }}
    )
    """
    pass

def rollback():
    """
    Implementar rollback da migration (opcional).
    """
    pass
'''.format(name=name, date=__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template)
        
        self._log('info', f'Migration criada: {filename}')
        return filename

# Instância singleton
migration_manager = MigrationManager()
