import math

lado_a = float(input("Ingrese el lado A: "))
base = float(input("Ingrese la base: "))
hipotenusa = math.sqrt(lado_a ** 2 + base ** 2)

area_t = (lado_a * base) / 2
perimetro = lado_a + base + hipotenusa

print(f'El area del triangulo es: {area_t:.2f}')
print(f'El perimetro del triangulo es: {perimetro:.2f}')