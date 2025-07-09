from .figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado, lado2):
        super().__init__(lado)
        self._base = base
        self._altura = altura
        self._lado2 = lado2

    def area(self):
        return (self._base * self._altura) / 2

    def perimetro(self):
        return self._base + self._lado + self._lado2

    def __str__(self):
        return f'El triángulo tiene área: {self.area()} y perímetro: {self.perimetro()}'
