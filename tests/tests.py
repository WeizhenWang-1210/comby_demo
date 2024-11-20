import unittest
class MyTestCase(unittest.TestCase):
    def test_add(self):
        from lib.ComplexNumber import ComplexNumber
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(2, 3)
        old_c1 = ComplexNumber(1, 2)
        old_c2 = ComplexNumber(2, 3)
        sum = c1 + c2
        self.assertEqual(c1, old_c1)
        self.assertEqual(c2, old_c2)
        self.assertEqual(sum, ComplexNumber(3,5))

    def test_multiply(self):
        from lib.ComplexNumber import ComplexNumber
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(2, 3)
        old_c1 = ComplexNumber(1, 2)
        old_c2 = ComplexNumber(2, 3)
        prod = c1 * c2
        self.assertEqual(c1, old_c1)
        self.assertEqual(c2, old_c2)
        self.assertEqual(prod, ComplexNumber(-4, 7))


    def test_conjugate(self):
        from lib.ComplexNumber import ComplexNumber
        c1 = ComplexNumber(1, 2)
        old_c1 = ComplexNumber(1, 2)
        conjugate = c1.conjugate()
        target = ComplexNumber(1, -2)
        self.assertEqual(c1, old_c1)
        self.assertEqual(conjugate, target)




if __name__ == '__main__':
    unittest.main()
