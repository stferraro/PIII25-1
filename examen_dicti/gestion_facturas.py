def agrega_factura():
    """
    Agrega una nueva factura a la lista de facturas.
    """
    facturas = {}
    numero = input("Número de factura(o 'fin' para terminar): ")
    while numero != "fin":
        valor = float(input("Valor de la factura: "))
        facturas[numero] = valor
        numero = input("Número de factura (o 'fin' para terminar): ")
    return facturas

def pagar_factura(facturas):
    """
    Paga una factura de la lista de facturas.
    """
    numero = input("Número de factura a pagar: ")
    if numero in facturas:
        monto = float(input("Monto a pagar: "))
        while monto > facturas.get(numero) or monto < 0:
            print("El monto a pagar es mayor que el valor de la factura.")
            monto = float(input("Monto a pagar: "))
        valor = facturas.get(numero)
        monto_total = valor - monto
        facturas[numero] = monto_total
    return facturas

def ver_facturas(facturas):
    """
    Muestra todas las facturas y su estado.
    """
    print("Facturas:")
    for numero, valor in facturas.items():
        print(f"Factura {numero}: ${valor:.2f}")
        
def total_facturas(facturas):
    """
    Calcula el total de todas las facturas.
    """
    return sum(facturas.values())

def menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("Opciones:")
    print("1. Pagar factura")
    print("2. Ver facturas")
    print("3. Total de facturas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    """
    Función principal para gestionar las facturas.
    """
    print("Bienvenido al sistema de gestión de facturas.")
    facturas = agrega_factura()
    while True:
        opcion = menu()
        if opcion == "1":
            facturas = pagar_factura(facturas)
        elif opcion == "2":
            ver_facturas(facturas)
        elif opcion == "3":
            total = total_facturas(facturas)
            print(f"Total de facturas: ${total:.2f}")
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
main()