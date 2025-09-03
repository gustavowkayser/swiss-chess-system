class Rating:
    def __init__(
        self,
        rating_classico: int,
        rating_rapido: int,
        rating_blitz: int
    ):
        self.__rating_classico = rating_classico
        self.__rating_rapido = rating_rapido
        self.__rating_blitz = rating_blitz

    @property
    def rating_classico(self):
        return self.__rating_classico

    @rating_classico.setter
    def rating_classico(self, value):
        self.__rating_classico = value

    @property
    def rating_rapido(self):
        return self.__rating_rapido

    @rating_rapido.setter
    def rating_rapido(self, value):
        self.__rating_rapido = value

    @property
    def rating_blitz(self):
        return self.__rating_blitz

    @rating_blitz.setter
    def rating_blitz(self, value):
        self.__rating_blitz = value