import math

class ComplexNumber:
    def __init__(self, real, imag):
        """
        Initialize a complex number with a real and imaginary part.
        """
        self.real = real
        self.imag = imag

    def __str__(self):
        """
        Return a string representation of the complex number.
        """
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    def __add__(self, other):
        """
        Add two complex numbers.
        """
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """
        Subtract one complex number from another.
        """
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """
        Multiply two complex numbers.
        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        """
        Divide one complex number by another.
        """
        denom = other.real**2 + other.imag**2
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def conjugate(self):
        """
        Return the conjugate of the complex number.
        """
        return ComplexNumber(self.real, -self.imag)

    def __eq__(self, other):
        """
        Check if two complex numbers are equal.
        """
        return self.real == other.real and self.imag == other.imag



