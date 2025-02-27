#constantes -- descuentos y IVA

DESC_TOMATE = 0.2
DESC_ZANAHORIA = 0.3
DESC_CALABACIN = 0.5
DESC_BERENJENA = 0.4
IVA = 0.16

# variables

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

precio_tomates = float(input("Ingrese el precio de los tomates: "))
precio_zanahorias = float(input("Ingrese el precio de las zanahorias: "))
precio_calabacines = float(input("Ingrese el precio de los calabacines: "))
precio_berenjenas = float(input("Ingrese el precio de las berenjenas: "))

kg_tomates = float(input("Ingrese la cantidad de kilos de tomates: "))
kg_zanahorias = float(input("Ingrese la cantidad de kilos de zanahorias: "))
kg_calabacines = float(input("Ingrese la cantidad de kilos de calabacines: "))
kg_berenjenas = float(input("Ingrese la cantidad de kilos de berenjenas: "))

#operaciones
total_tomates = precio_tomates * kg_tomates
total_zanahorias = precio_zanahorias * kg_zanahorias
total_calabacines = precio_calabacines * kg_calabacines
total_berenjenas = precio_berenjenas * kg_berenjenas

descuento_tomates = total_tomates - (total_tomates * DESC_TOMATE)
descuento_zanahorias = total_zanahorias - (total_zanahorias * DESC_ZANAHORIA)
descuento_calabacines = total_calabacines - (total_calabacines * DESC_CALABACIN)
descuento_berenjenas = total_berenjenas - (total_berenjenas * DESC_BERENJENA)

total_descuento = descuento_tomates + descuento_zanahorias + descuento_calabacines + descuento_berenjenas
total_IVA = total_descuento + (total_descuento * IVA)

print(f'El total a pagar por {nombre} {apellido} es: {total_IVA:.2f} $')

