class Contabilidad:
    
    def __init__(self):
        self.__facturas = {}

    def agregar_factura(self, numero, monto):
        if numero not in self.__facturas:
            self.__facturas[numero] = monto
        return self.__facturas

    def pagar_factura(self):
        numero = input("Numero de factura: ")
        if numero not in self.__facturas.keys():
            print("Factura no encontrada.")
        else:
            monto = float(input("Monto a Pagar: "))
            valor = self.__facturas.get(numero)
            while monto > valor or monto < 0:
                print("El monto a pagar es mayor que el valor de la factura.")
                monto = float(input("Monto a cancelar: "))
            pago = valor - monto 
            self.__facturas[numero] = pago
        return self.__facturas

    def mostrar_facturas(self):
        print(self.__facturas)

class Factura:
    
    def __init__(self, numero, monto):
        self.__numero = numero
        self.__monto = monto

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def _monto(self):
        return self.__monto

    @_monto.setter
    def _monto(self, value):
        self.__monto = value
        
    def __str__(self):
        return f"Factura {self.__numero}: ${self.__monto:.2f}"
    
    def __repr__(self):
        return f"Factura {self.__numero}: ${self.__monto:.2f}"
    
def main():
    
    contabilidad = Contabilidad()
    while True:
        print("Opciones:")
        print("1. Agregar factura")
        print("2. Pagar factura")
        print("3. Mostrar facturas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            numero = input("Número de factura: ")
            monto = float(input("Monto de la factura: "))
            contabilidad.agregar_factura(numero, monto)
        elif opcion == "2":
            contabilidad.pagar_factura()
        elif opcion == "3":
            contabilidad.mostrar_facturas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
            
main()