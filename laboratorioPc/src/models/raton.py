from src.models.dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    
    contador_ratones = 0
    
    def __init__(self, marca: str, tipoEntrada: str):
        Raton.contador_ratones += 1
        self.__idRaton = Raton.contador_ratones
        super().__init__(marca, tipoEntrada)

    @property
    def _idRaton(self):
        return self.__idRaton

    @_idRaton.setter
    def _idRaton(self, value):
        self.__idRaton = value
        super().__init__(marca, tipoEntrada)
        
    def __str__(self):
        return f'Raton(id:{self.__idRaton}, marca={self._marca}, tipoEntrada={self._tipoEntrada})'
