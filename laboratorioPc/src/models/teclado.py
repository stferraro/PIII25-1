# coding: utf-8

from src.models.dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contador_teclados = 0
    
    def __init__(self, marca: str, tipoEntrada: str, idioma: str):
        Teclado.contador_teclados += 1
        self.__idTeclado = Teclado.contador_teclados
        self.__idioma = idioma
        super().__init__(marca, tipoEntrada)

    @property
    def _idTeclado(self):
        return self.__idTeclado

    @_idTeclado.setter
    def _idTeclado(self, value):
        self.__idTeclado = value

    @property
    def _idioma(self):
        return self.__idioma

    @_idioma.setter
    def _idioma(self, value):
        self.__idioma = value

        
    def __str__(self):
        return f'Teclado(id:{self.__idTeclado}, marca={self._marca}, tipoEntrada={self._tipoEntrada}, idioma={self.__idioma})'