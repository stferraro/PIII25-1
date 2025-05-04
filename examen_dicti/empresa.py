class Actividad:
    
    def __init__(self, descripcion, horas):
        self.__descripcion = descripcion
        self.__horas = horas

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

    @property
    def _horas(self):
        return self.__horas

    @_horas.setter
    def _horas(self, value):
        self.__horas = value

    def __str__(self):
        return f"Descripcion: {self.__descripcion}, Horas: {self.__horas}"


class Trabajador:
    
    def __init__(self, cedula, nombre, telefono, actividad):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__telefono = telefono
        self.__actividad = actividad


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
        
    @property
    def _actividad(self):
        return self.__actividad

    @_actividad.setter
    def _actividad(self, value):
        self.__actividad = value

    def __str__(self):
        return f"Nombre: {self.__nombre}, Telefono: {self.__telefono}, Cedula: {self.__cedula} Actividad: {self.__actividad.__str__()}"
    
def menu():
    print("1. Agregar trabajador")
    print("2. Asignar actividad")
    print("3. Mostrar trabajadores")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    while opcion < 1 or opcion > 4:
        opcion = int(input("Opción inválida. Ingrese una opción: "))
    return opcion

  
def main():
    opcion = menu() 
    while opcion != 4:
        if opcion == 1:
            cedula = input("Ingrese la cédula del trabajador: ")
            nombre = input("Ingrese el nombre del trabajador: ")
            telefono = input("Ingrese el teléfono del trabajador: ")
            actividad = Actividad("", 0)
            trabajador = Trabajador(cedula, nombre, telefono, actividad)
            print(f"Trabajador {nombre} agregado.")
        elif opcion == 2:
            cedula = input("Ingrese la cédula del trabajador: ")
            if trabajador._cedula == cedula:
                descripcion = input("Ingrese la descripción de la actividad: ")
                horas = float(input("Ingrese las horas de la actividad: "))
                actividad._descripcion = descripcion
                actividad._horas = horas
                trabajador._actividad = actividad
                print(f"Actividad {descripcion} asignada al trabajador {trabajador._nombre}.")
            else:
                print("Cédula no encontrada.")
        elif opcion == 3:
            print("Trabajadores:")
            print(trabajador.__str__())
        else:
            print("Opción no válida.")
        opcion = menu()
    print("Saliendo del programa...")
            
    
main()