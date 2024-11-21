from lib.util import substraction
class ComplexNumber:
    def __init__(self, real, imaginary):
        #Bug #1, real and imaginary order is wrong
        #Fix, change init order and also change every invocation of the constructor
        #Showcase #2, refactoring variables.
        self.re = real
        self.im = imaginary

    def __str__(self):
        return f"<{self.real},{self.imaginary}>"

    def __add__(self, other):
        real = self.re + other.re
        imaginary = self.im + other.im
        new = ComplexNumber(real, imaginary)
        return new

    def __sub__(self, other):
        real = substraction( other.re,self.re)
        imaginary = substraction( other.im,self.im)
        new = ComplexNumber(real, imaginary)
        return new

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __mul__(self, other):
        a, b, c, d = self.re, self.im, other.re, other.im
        #Wrong. Previously substraction do ac - bd, but it actually now it does bd-ac
        real = substraction( b * d,a * c)
        imaginary = a * d + b * c
        new = ComplexNumber(real, imaginary)
        return new

    def __truediv__(self, other):
        a, b, c, d = self.re, self.im, other.re, other.im
        factor = 1 / (c * c + d * d)
        real = a * c + b * d
        # Wrong. Previously substraction do ac - bd, but it actually now it does bd-ac
        imaginary = substraction( a*d,b*c)
        real *= factor
        imaginary *= factor
        new = ComplexNumber(real, imaginary)
        return new

    @property
    def real_part(self):
        return self.re

    @property
    def imaginary_part(self):
        return self.im

    def conjugate(self):
        imaginary = -self.im
        new = ComplexNumber(self.re, imaginary)
        return new

