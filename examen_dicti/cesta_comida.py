class Persona:
    
    def __init__(self, nombre, apellido, cedula, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__telefono = telefono

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
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value
        
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} - {self.__cedula} - {self.__telefono}"
    
    def __repr__(self):
        return f"{self.__nombre} {self.__apellido} - {self.__cedula} - {self.__telefono}"

class Producto:
    
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    def __str__(self):
        return f"{self.__nombre}: {self.__precio}"
    
    def __repr__(self):
        return f"{self.__nombre}: {self.__precio}"

class Cesta:
    
    def __init__(self):
        self.__productos = {}
        
    def agregar_producto(self, producto, precio):
        if producto in self.__productos:
            self.__productos[producto] += precio
        else:
            self.__productos[producto] = precio
            
    def calcular_total(self):
        total = 0
        for precio in self.__productos.values():
            total += precio
        total_con_iva = total * 1.16
        return total_con_iva
    
    def __str__(self):
        return f"Productos en la cesta: {self.__productos}"
    
    def __repr__(self):
        return f"Productos en la cesta: {self.__productos}"
    
def main():
    """
    Main function to run the shopping basket program.
    """
    print("Welcome to the shopping basket program!")
    
    nombre = input(("Nombre: "))
    apellido = input("Apellido: ")
    cedula = input("Cedula: ")
    telefono = input("Telefono: ")
    
    persona = Persona(nombre, apellido, cedula, telefono)
    print(f"Persona: {persona}")
    
    cesta = Cesta()
    
    while True:
        producto = input("Producto: ")
        if producto.lower() == 'salir':
            break
        
        precio = float(input("Precio: "))
        cesta.agregar_producto(producto, precio)
        
    total = cesta.calcular_total()
    print(f"Total de la cesta: {total:.2f}")
    
if __name__ == "__main__":
    main()
    
    
    