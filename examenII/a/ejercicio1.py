edad = int(input("Ingrese su edad: "))

precio = 0

if edad < 4:
    precio = 0
elif edad >= 4 and edad <= 18:
    precio = 5
else:
    precio = 10
    
print(f'El precio a pagar es: {precio} $')
