import unittest
from lib.ComplexNumber import ComplexNumber
class MyTestCase(unittest.TestCase):
    def test_initialization(self):
        c1 = ComplexNumber(1, 2)
        self.assertEqual(c1.re, 1)
        self.assertEqual(c1.im, 2)

    def test_property(self):
        c1 = ComplexNumber(1, 2)
        self.assertEqual(c1.real_part, c1.re)
        self.assertEqual(c1.imaginary_part, c1.im)

    def test_add(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(2, 3)
        sum = c1 + c2
        self.assertEqual(sum, ComplexNumber(3,5))

    def test_substract(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(2, 3)
        diff = c1 - c2
        self.assertEqual(diff, ComplexNumber(-1,-1))
        
    def test_multiply(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(2, 3)
        prod = c1 * c2
        self.assertEqual(prod, ComplexNumber(-4, 7))
        
    def test_divide(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(2, 3)
        div = c1 / c2
        self.assertEqual(div, ComplexNumber(8/13, 1/13))
        
    def test_conjugate(self):
        c1 = ComplexNumber(1, 2)
        conjugate = c1.conjugate()
        target = ComplexNumber(1, -2)
        self.assertEqual(conjugate, target)




if __name__ == '__main__':
    unittest.main()
