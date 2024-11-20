class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"<{self.real},{self.imaginary}>"

    def __add__(self, other):
        self.real += other.real
        self.imaginary += other.imaginary
        new = ComplexNumber(self.real, self.imaginary)
        return new

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __mul__(self, other):
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        self.real = a * c - b * d
        self.imaginary = a * d + b * c
        new = ComplexNumber(self.real, self.imaginary)
        return new

    def __truediv__(self, other):
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        factor = 1 / (c * c + d * d)
        self.real = a * c + b * d
        self.imaginary = b * c - a * d
        self.real *= factor
        self.imaginary *= factor
        new = ComplexNumber(self.real, self.imaginary)
        return new

    def real(self):
        return self.real

    def imaginary(self):
        return self.imaginary

    def conjugate(self):
        self.imaginary = -self.imaginary
        new = ComplexNumber(self.real, self.imaginary)
        return new

