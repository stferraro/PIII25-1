from src.models.triangulo import Triangulo
from src.models.cuadrado import Cuadrado

lado = float(input('Lado del cuadrado: '))
cuadrado = Cuadrado(lado)
print(cuadrado)
lado2 = float(input('Lado2: '))
base = float(input('Base: '))
altura = float(input('Altura: '))
triangulo = Triangulo(base, altura, lado, lado2)
print(triangulo)