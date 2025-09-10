from typing import Dict
from enum import Enum
from typing import Optional

class LogLevel(Enum):
    DEBUG = "DEBUG"
    DEFAULT = "DEFAULT"

class Logger:
    def __init__(self, log_level: LogLevel):
        self.log_level = log_level

    def debug(self, message: str, context: Optional[Dict] = None):
        if self.log_level == LogLevel.DEBUG:
            print(f"DEBUG: {message}" + (f" | Context: {context}" if context else ""))

    def info(self, message: str, context: Optional[Dict] = None):
        print(f"INFO: {message}" + (f" | Context: {context}" if context else ""))

    def error(self, message: str, context: Optional[Dict] = None):
        print(f"ERROR: {message}" + (f" | Context: {context}" if context else ""))