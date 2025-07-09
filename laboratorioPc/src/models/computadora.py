from src.models.raton import Raton
from src.models.teclado import Teclado
from src.models.monitor import Monitor
from src.models.impresora import Impresora

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre: str, raton: Raton, teclado: Teclado, monitor: Monitor, impresora: Impresora):
        Computadora.contador_computadoras += 1
        self.__idComputadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__raton = raton
        self.__teclado = teclado
        self.__monitor = monitor
        self.__impresora = impresora

    @property
    def _idComputadora(self):
        return self.__idComputadora

    @_idComputadora.setter
    def _idComputadora(self, value):
        self.__idComputadora = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _raton(self):
        return self.__raton

    @_raton.setter
    def _raton(self, value):
        self.__raton = value

    @property
    def _teclado(self):
        return self.__teclado

    @_teclado.setter
    def _teclado(self, value):
        self.__teclado = value

    @property
    def _monitor(self):
        return self.__monitor

    @_monitor.setter
    def _monitor(self, value):
        self.__monitor = value

    @property
    def _impresora(self):
        return self.__impresora

    @_impresora.setter
    def _impresora(self, value):
        self.__impresora = value

        
    

    def __str__(self):
        return (f'Computadora(id:{self.__idComputadora}, nombre={self.__nombre}, '
                f'raton={self.__raton}, teclado={self.__teclado}, '
                f'monitor={self.__monitor}, impresora={self.__impresora})')