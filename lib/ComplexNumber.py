from lib.util import substraction
class ComplexNumber:
    def __init__(self, imaginary, real):
        #Bug #1, real and imaginary order is wrong
        #Fix, change init order and also change every invocation of the constructor
        #Showcase #2, refactoring variables.
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"<{self.real},{self.imaginary}>"

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        new = ComplexNumber(real, imaginary)
        return new

    def __sub__(self, other):
        real = substraction(self.real, other.real)
        imaginary = substraction(self.imaginary, other.imaginary)
        new = ComplexNumber(real, imaginary)
        return new

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __mul__(self, other):
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        #Wrong. Previously substraction do ac - bd, but it actually now it does bd-ac
        real = substraction(a * c, b * d)
        imaginary = a * d + b * c
        new = ComplexNumber(real, imaginary)
        return new

    def __truediv__(self, other):
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        factor = 1 / (c * c + d * d)
        real = a * c + b * d
        # Wrong. Previously substraction do ac - bd, but it actually now it does bd-ac
        imaginary = substraction(b*c, a*d)
        real *= factor
        imaginary *= factor
        new = ComplexNumber(real, imaginary)
        return new

    def real_part(self):
        #showcase #3, adding property decorator
        return self.real

    def imaginary_part(self):
        return self.imaginary

    def conjugate(self):
        imaginary = -self.imaginary
        new = ComplexNumber(self.real, imaginary)
        return new

