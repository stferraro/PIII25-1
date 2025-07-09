from .figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado)

    def area(self):
        return self._lado ** 2

    def perimetro(self):
        return 4 * self._lado

    def __str__(self):
        return f'El cuadrado tiene área: {self.area()} y perímetro: {self.perimetro()}'