from lib.ComplexNumber import ComplexNumber

if __name__ == '__main__':
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(2, 3)
    old_c1, old_c2 = c1, c2
    prod = c1 * c2
    print(c1, c2)
