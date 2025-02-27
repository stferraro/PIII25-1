DESC = 0.12
IVA = 0.16

precio_product_1 = float(input("Ingrese el precio del producto 1: "))
precio_product_2 = float(input("Ingrese el precio del producto 2: "))
precio_product_3 = float(input("Ingrese el precio del producto 3: "))
precio_product_4 = float(input("Ingrese el precio del producto 4: "))

cantidad_product_1 = int(input("Ingrese la cantidad del producto 1: "))
cantidad_product_2 = int(input("Ingrese la cantidad del producto 2: "))
cantidad_product_3 = int(input("Ingrese la cantidad del producto 3: "))
cantidad_product_4 = int(input("Ingrese la cantidad del producto 4: "))

subtotal_1 = precio_product_1 * cantidad_product_1
subtotal_2 = precio_product_2 * cantidad_product_2
subtotal_3 = precio_product_3 * cantidad_product_3
subtotal_4 = precio_product_4 * cantidad_product_4

total = subtotal_1 + subtotal_2 + subtotal_3 + subtotal_4
descuento_total = total - (total * DESC)
precio_final = descuento_total + (descuento_total * IVA)

print(f'El total a pagar es: {precio_final:.2f}')
