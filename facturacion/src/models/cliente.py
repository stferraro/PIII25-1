class Cliente:
    
    def __init__(self, nombre, apellido, cedula):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value
        
    def __str__(self):
        return f'{self.__nombre} - {self.__apellido} - {self.__cedula}'
    
    
 