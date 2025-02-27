import math

lado_a = float(input("Ingrese el lado A: "))
lado_b = float(input("Ingrese el lado B: "))
angulo = float(input("Ingrese el angulo en grados: "))

angulo_rad = math.radians(angulo)

area = (lado_a * lado_b * math.sin(angulo_rad)) / 2
lado_3 = math.sqrt(lado_a ** 2 + lado_b ** 2 - 2 * lado_a * lado_b * math.cos(angulo_rad))

perimetro = lado_a + lado_b + lado_3

print(f'El area del triangulo es: {area:.2f}')
print(f'El perimetro del triangulo es: {perimetro:.2f}')