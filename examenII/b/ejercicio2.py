import math

lado_a = float(input("Ingrese el lado A: "))
lado_b = float(input("Ingrese el lado B: "))
lado_c = float(input("Ingrese el lado C: "))

if ((lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a):
    
    if lado_a == lado_b and lado_a == lado_c:
        print("El triangulo es equilatero")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")
    
    perimetro = lado_a + lado_b + lado_c
    s = perimetro / 2
    det = s * (s - lado_a) * (s - lado_b) * (s - lado_c)
    if det > 0:
        area = math.sqrt(det)
        print(f'El area del triangulo es: {area:.2f}')
    else:
        print("No se puede calcular el area del triangulo")
    print(f'El perimetro del triangulo es: {perimetro:.2f}')
    
else:
    print("No es un triangulo")