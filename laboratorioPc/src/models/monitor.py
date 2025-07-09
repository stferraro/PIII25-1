from src.models.dispositivo_salida import DispositivoSalida

class Monitor(DispositivoSalida):
    
    contador_monitores = 0
    
    def __init__(self, marca: str, tipoSalida: str, tamaño: str, resolucion: str):
        Monitor.contador_monitores += 1
        self.__idMonitor = Monitor.contador_monitores
        self.__tamaño = tamaño
        self.__resolucion = resolucion
        super().__init__(marca, tipoSalida)

    @property
    def _idMonitor(self):
        return self.__idMonitor

    @_idMonitor.setter
    def _idMonitor(self, value):
        self.__idMonitor = value

    @property
    def _tamaño(self):
        return self.__tamaño

    @_tamaño.setter
    def _tamaño(self, value):
        self.__tamaño = value

    @property
    def _resolucion(self):
        return self.__resolucion

    @_resolucion.setter
    def _resolucion(self, value):
        self.__resolucion = value


    def __str__(self):
        return f'Monitor(id:{self.__idMonitor}, marca={self._marca}, tipoSalida={self._tipoSalida}, tamaño={self.__tamaño}, resolucion={self.__resolucion})'