DESC = 0.15
IVA = 0.16

precio_pan = float(input("Ingrese el precio del pan: "))
precio_aceite = float(input("Ingrese el precio del aceite: "))
precio_queso = float(input("Ingrese el precio del queso: "))
precio_jamon = float(input("Ingrese el precio del jamón: "))

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

total = precio_pan + precio_aceite + precio_queso + precio_jamon
total_descuento = total - (total * DESC)
total_IVA = total_descuento + (total_descuento * IVA)

print(f'El total a pagar por {nombre} {apellido} es: {total_IVA:.2f} $')