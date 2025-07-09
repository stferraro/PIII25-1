from src.models.cliente import Cliente
from src.models.factura import Factura

nombre = input('Nombre: ')
apellido = input('Apellido: ')
cedula = input('Cedula:')
cliente = Cliente(nombre, apellido, cedula)
factura = Factura(cliente)
print(factura)