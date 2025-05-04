class Usuario:
    
    def __init__(self, cedula, nombre, edad, membresia):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__edad = edad
        self.__membresia = membresia

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value
        
    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _edad(self):
        return self.__edad

    @_edad.setter
    def _edad(self, value):
        self.__edad = value

    @property
    def _membresia(self):
        return self.__membresia

    @_membresia.setter
    def _membresia(self, value):
        self.__membresia = value
        
    def get_pago(self):
        if self.__membresia == 'Mensual':
            pago = 20
        elif self.__membresia == 'Trimestral':
            pago = 55
        elif self.__membresia == 'Anual':
            pago = 200
        else:
            pago = 0
        return pago
            
        
    def __str__(self):
        return f'cedula: {self.__cedula} nombre: {self.__nombre} edad{self.__edad} membresia: {self.__membresia}'

class Gimnasio:
    
    def __init__(self, usuarios):
        self.__usuarios = usuarios

    @property
    def _usuarios(self):
        return self.__usuarios

    @_usuarios.setter
    def _usuarios(self, value):
        self.__usuarios = value
        
    def agrega_usuario(self, usuario):
        self.__usuarios.append(usuario)
        
    def __str__(self) :
        return self.__usuarios.__str__()
    
    
def menu():
    print('Sistema de Gestion de un Gimnasio')
    print('1. agrega usuario')
    print('2. Calcular Membresia')
    print('3. Salir')
    opcion = int(input('Opcion a realizar(3 para salir: )'))
    while opcion < 1 or opcion > 3:
        opcion = int(input('Error, Opcion a realizar(3 para salir: )'))
    return opcion
    
def main():
    opcion = menu()
    gimnasio = Gimnasio(usuarios = [])
    while opcion != 3:
        if opcion == 1:
            cedula = input('Cedula: ')
            nombre = input('Nombre: ')
            edad = int(input('edad: '))
            while edad < 0 :
                edad = int(input('edad: '))
            membresia = input('membresia: ')
            while membresia not in ('Mensual', 'Anual', 'Trimestral'):
                membresia = input('membresia (Mensual, Anual, Trimestral): ')
            usuario = Usuario(cedula, nombre, edad, membresia)
            gimnasio.agrega_usuario(usuario)
        elif opcion == 2:
            users = gimnasio._usuarios
            for user in users:
                cedula = input("Cedula del Usuario: ")
                if user._cedula == cedula:
                    membresia = user.get_pago()
                    print(membresia)
                else:
                    print('Usuario no registrado')
        elif opcion == 3:
            break
        opcion = menu()


main()
            
        
        
    
    