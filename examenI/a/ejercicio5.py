import math

diametro = float(input("Ingrese el diámetro del cono: "))
generatriz = float(input("Ingrese la generatriz del cono: "))

radio = diametro / 2
h = math.sqrt(radio ** 2 + generatriz ** 2)

area = math.pi * radio * (radio + generatriz)
volumen = (math.pi * radio ** 2 * h) / 3

print(f'El area del cono es: {area:.2f}')
print(f'El volumen del cono es: {volumen:.2f}')