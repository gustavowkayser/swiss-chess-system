from app.utils.enums import TipoDesempate

class Desempate:
    def __init__(self, tipo: TipoDesempate, valor: float):
        self.tipo = tipo
        self.valor = valor

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, value):  
        self.__valor = value