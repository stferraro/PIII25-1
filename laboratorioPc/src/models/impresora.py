from src.models.dispositivo_salida import DispositivoSalida

class Impresora(DispositivoSalida):
    
    contador_impresoras = 0
    
    def __init__(self, marca: str, tipoSalida: str, modelo: str):
        Impresora.contador_impresoras += 1
        self.__idImpresora = Impresora.contador_impresoras
        self.__modelo = modelo
        super().__init__(marca, tipoSalida)

    @property
    def _idImpresora(self):
        return self.__idImpresora

    @_idImpresora.setter
    def _idImpresora(self, value):
        self.__idImpresora = value

    @property
    def _modelo(self):
        return self.__modelo

    @_modelo.setter
    def _modelo(self, value):
        self.__modelo = value

    def __str__(self):
        return f'Impresora(id:{self.__idImpresora}, marca={self._marca}, tipoSalida={self._tipoSalida}, modelo={self.__modelo})'