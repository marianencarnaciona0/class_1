class Shape:
    def __init__(self, lados):
        self.lados = lados


class Circulo(Shape):
    def __init__(self, radio):
        super().__init__(0)
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.radio


circulo = Circulo(4)
print(circulo.area())
print(circulo.perimetro())


class Rectangle(Shape):
    def __init__(self, longitud, ancho):
        super().__init__(4)
        self.longitud = longitud
        self.ancho = ancho

    def area(self):
        return self.longitud * self.ancho

    def perimetro(self):
        return 2 * (self.longitud + self.ancho)


rectangulo = Rectangle(5, 3)
print(rectangulo.area())
print(rectangulo.perimetro())


class Triangulo(Shape):
    def __init__(self, base, altura, ladoA, ladoB, ladoC):
        super().__init__(3)
        self.base = base
        self.altura = altura
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def area(self):
        return 0.5 * self.base * self.altura

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC


triangulo = Triangulo(4, 3, 3, 6, 8)
print(triangulo.area())
print(triangulo.perimetro())