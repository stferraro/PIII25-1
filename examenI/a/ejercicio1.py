precio_tv = float(input("Ingrese el precio de la televisión: "))
precio_lavadora = float(input("Ingrese el precio de la lavadora: "))
precio_comp = float(input("Ingrese el precio del computador: "))
precio_licuadora = float(input("Ingrese el precio de la licuadora: "))
precio_router = float(input("Ingrese el precio del router: "))

total = precio_tv + precio_lavadora + precio_comp + precio_licuadora + precio_router
precio_descontado = total - (total * 0.15)
precio_total = precio_descontado + (precio_descontado * 0.16)

print(f'El precio total es: {precio_total:.2f} $$')