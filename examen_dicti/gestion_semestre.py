class Estudiante:
    
    def __init__(self, nombre, apellido, cedula, codigo_universitario, materias):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__codigo_universitario = codigo_universitario
        self.__materias = materias

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

    @property
    def _codigo_universitario(self):
        return self.__codigo_universitario

    @_codigo_universitario.setter
    def _codigo_universitario(self, value):
        self.__codigo_universitario = value

    @property
    def _materias(self):
        return self.__materias

    @_materias.setter
    def _materias(self, value):
        self.__materias = value
        
    def agregar_materia(self, materia):
        self.__materias.append(materia)
        
    def calcular_promedio(self):
        if not self.__materias:
            return 0
        total_nota = sum(materia._nota for materia in self.__materias)
        return total_nota / len(self.__materias)
    
    def verificar_aprobacion(self):
        promedio = self.calcular_promedio()
        if promedio >= 10:
            return "Aprobado"
        else:
            return "Reprobado"
        
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Cedula: {self.__cedula}, Codigo Universitario: {self.__codigo_universitario}, Materias: {self.__materias}"
    
    def __repr__(self) -> str:
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Cedula: {self.__cedula}, Codigo Universitario: {self.__codigo_universitario}, Materias: {self.__materias}"
    
class Materia:
    
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _nota(self):
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value
        
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, Nota: {self.__nota}"
    
    def __repr__(self) -> str:
        return f"Nombre: {self.__nombre}, Nota: {self.__nota}"

def menu():
    print("1. Agregar estudiante")
    print("2. Agregar materia")
    print("3. Calcular promedio")
    print("4. Verificar aprobacion")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
    
def main():
    opcion = menu()
    while opcion != "5":
        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            cedula = input("Ingrese la cedula del estudiante: ")
            codigo_universitario = input("Ingrese el codigo universitario del estudiante: ")
            materias = []
            estudiante = Estudiante(nombre, apellido, cedula, codigo_universitario, materias)
            print(f"Estudiante agregado: {estudiante}")
        elif opcion == "2":
            nombre_materia = input("Ingrese el nombre de la materia: ")
            nota_materia = float(input("Ingrese la nota de la materia: "))
            materia = Materia(nombre_materia, nota_materia)
            estudiante.agregar_materia(materia)
            print(f"Materia agregada: {materia}")
        elif opcion == "3":
            promedio = estudiante.calcular_promedio()
            print(f"Promedio del estudiante: {promedio}")
        elif opcion == "4":
            estado = estudiante.verificar_aprobacion()
            print(f"Estado del estudiante: {estado}")
        else:
            print("Opción no válida")
        opcion = menu()
        if opcion == "5":
            print("Saliendo del programa...")
            break
        
main()
        

    
    
