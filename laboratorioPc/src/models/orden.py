from src.models.computadora import Computadora

class Orden:
    
    contador_ordenes = 0

    def __init__(self, computadoras: list[Computadora]):
        Orden.contador_ordenes += 1
        self.__idOrden = Orden.contador_ordenes
        self.__computadoras = computadoras

    @property
    def _idOrden(self):
        return self.__idOrden

    @_idOrden.setter
    def _idOrden(self, value):
        self.__idOrden = value

    @property
    def _computadoras(self):
        return self.__computadoras

    @_computadoras.setter
    def _computadoras(self, value):
        self.__computadoras = value

        
    def agregar_computadora(self, computadora: Computadora):
        self.__computadoras.append(computadora)
        
    def imprimir_orden(self):
        with open(f'orden_{self.__idOrden}.txt', 'w') as file:
            file.write(str(self))

    def __str__(self):
        Computadoras_str = ''
        for computadora in self.__computadoras:
            Computadoras_str += f'\n\t{computadora}'
        return f'Orden(id:{self.__idOrden}, computadoras=[{Computadoras_str}])'