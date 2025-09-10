from .logger import Logger
from typing import TypeVar
from app.utils.utils import convert_to_date
from datetime import date
import math

T = TypeVar('T')

class Request:
    def __init__(self, logger: Logger):
        self.logger = logger

    def get_input(self, prompt: str, expected_type: T, **kwargs) -> T:
        while True:
            user_input = input(prompt)
            try:
                if expected_type == str and len(user_input) > kwargs.get("max_length", math.inf):
                    self.logger.error(f"Entrada muito longa. O máximo permitido é {kwargs.get('max_length', math.inf)} caracteres.")
                    continue
                if expected_type == str and len(user_input) < kwargs.get("min_length", 0):
                    self.logger.error(f"Entrada muito curta. O mínimo necessário é {kwargs.get('min_length', 0)} caracteres.")
                    continue
                if expected_type == date:
                    output = convert_to_date(user_input)
                    if output is None:
                        self.logger.error("Data inválida. Por favor, insira uma data no formato DD/MM/AAAA.")
                        continue
                    return output
                output = expected_type(user_input)
                if "choices" in kwargs and output not in kwargs["choices"]:
                    self.logger.error(f"Entrada inválida. As opções válidas são: {', '.join(map(str, kwargs['choices']))}.")
                    continue
                return output
            except ValueError:
                self.logger.error(f"Entrada inválida. Por favor, insira um {expected_type.__name__}.")