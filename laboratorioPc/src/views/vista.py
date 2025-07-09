from src.models.teclado import Teclado
from src.models.raton import Raton
from src.models.monitor import Monitor
from src.models.impresora import Impresora
from src.models.computadora import Computadora
from src.models.orden import Orden

valor = 'si'

while valor.lower() == 'si':
    
    print('1. Agregar teclado')
    print('2. Agregar raton')
    print('3. Agregar monitor')
    print('4. Agregar impresora')
    print('5. Agregar computadora')
    print('6. Imprimir orden')
    print('7. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        marca = input('Ingrese la marca del teclado: ')
        tipo_entrada = input('Ingrese el tipo de entrada del teclado: ')
        idioma = input('Ingrese el idioma del teclado: ')
        teclado = Teclado(marca, tipo_entrada, idioma)
        print(teclado)
    elif opcion == '2':
        marca = input('Ingrese la marca del ratón: ')
        tipo_entrada = input('Ingrese el tipo de entrada del ratón: ')
        raton = Raton(marca, tipo_entrada)
        print(raton)
    elif opcion == '3':
        marca = input('Ingrese la marca del monitor: ')
        tipo_salida = input('Ingrese el tipo de salida del monitor: ')
        resolucion = input('Ingrese la resolución del monitor: ')
        tamaño = input('Ingrese el tamaño del monitor: ')
        monitor = Monitor(marca, tipo_salida, tamaño, resolucion)
        print(monitor)
    elif opcion == '4':
        marca = input('Ingrese la marca de la impresora: ')
        tipo_salida = input('Ingrese el tipo de salida de la impresora: ')
        modelo = input('Ingrese el modelo de la impresora: ')
        impresora = Impresora(marca, tipo_salida, modelo)
        print(impresora)
    elif opcion == '5':
        marca = input('Ingrese la marca de la computadora: ')
        computadora = Computadora(marca, raton, teclado, monitor, impresora)
        print(computadora)
    elif opcion == '6':
        orden = Orden([computadora])
        orden.imprimir_orden()
    elif opcion == '7':
        valor = 'no'
    else:
        print('Opción no válida.')
        
    valor = input('¿Desea continuar? (si/no): ')
    if valor.lower() != 'si':
        print('Saliendo del programa...')
        break