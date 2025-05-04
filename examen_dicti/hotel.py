class Usuario:
    def __init__(self, cedula,nombre, telefono):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__telefono = telefono

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
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    def __str__(self):
        return f"Nombre: {self.__nombre}, Telefono: {self.__telefono}, Cedula: {self.__cedula}"
    
class Habitacion:
    
    def __init__(self, numero, estado):
        self.__numero = numero
        self.__estado = estado

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value
        
def menu():
    print("1. Agregar habitaciones")
    print("2. Registrar usuarios")
    print("3. Asignar habitación")
    print("4. Salir")
    opcion = int(input("Opcion a realizar (4 para salir): "))
    while opcion < 1 or opcion > 4:
        opcion = int(input("Error, Opcion a realizar (4 para salir): "))
    return opcion

def main():
    opcion = menu()
    habitaciones = {}
    usuarios = {}
    while opcion != 4:
        if opcion == 1:
            numero = input("Numero habitacion (fin para cerrar): ")
            while numero != "fin":
                estado = input("disponible/ocupada: ")
                while estado not in ("disponible", "ocupada"):
                    estado = input("Estado invalido, disponible/ocupada: ")
                habitaciones[numero] = Habitacion(numero, estado)
                numero = input("Numero habitacion (fin para cerrar): ")
        elif opcion == 2:
            cedula = input("Cedula: ")
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            usuarios[cedula] = Usuario(cedula, nombre, telefono)
        elif opcion == 3:
            numero = input("Numero habitacion (fin para cerrar): ")
            if numero == "fin":
                break
            estado = habitaciones.get(numero)
            if estado is None:
                print("Habitación no registrada. Intenta con otra.")
                continue

            if estado._estado == "disponible":
                cedula = input("Cedula: ")
                if cedula in usuarios.keys():
                    print(f"Habitación {numero} asignada a {usuarios[cedula]._nombre}")
                    habitaciones[numero]._estado = "ocupada"
                else:
                    print("Cédula no encontrada. Intenta nuevamente.")
            else:
                print("Habitación ocupada. Intenta con otra.")
        opcion = menu()

main()