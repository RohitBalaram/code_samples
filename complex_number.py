import unittest


class ComplexNumber(object):

    def __init__(self, complex_number):
        self.real = float(complex_number[0])
        self.imaginary = float(complex_number[1])

    def formatter(self, new_real, new_imaginary):
        if new_real == 0.0 and new_imaginary == 0.0:
            return "0.00"
        elif new_imaginary >= 0:
            if new_real == 0.0:
                return "{0:.2f}".format(float(new_imaginary)) + 'i'
            elif new_imaginary == 0.0:
                return "{0:.2f}".format(float(new_real))
            else:
                return ("{0:.2f}".format(float(new_real)) +
                        " + {0:.2f}".format(float(abs(new_imaginary))) + 'i')
        else:
            if new_real == 0.0:
                return "{0:.2f}".format(float(new_imaginary)) + 'i'
            elif new_imaginary == 0.0:
                return "{0:.2f}".format(float(new_real))
            else:
                return ("{0:.2f}".format(float(new_real)) +
                        " - {0:.2f}".format(float(abs(new_imaginary))) + 'i')

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return self.formatter(new_real, new_imaginary)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return self.formatter(new_real, new_imaginary)

    def __mul__(self, other):
        f = self.real * other.real
        l = (self.imaginary * other.imaginary) * -1
        o = self.real * other.imaginary
        i = self.imaginary * other.real

        new_real = float(f + l)
        new_imaginary = float(o + i)
        return self.formatter(new_real, new_imaginary)

    def __div__(self, other):
        f = self.real * other.real
        l = (self.imaginary * (other.imaginary * -1)) * -1
        o = self.real * (other.imaginary * -1)
        i = self.imaginary * other.real

        new_real = float(f + l)
        new_imaginary = float(o + i)

        df = other.real * other.real
        dl = (other.imaginary * (other.imaginary * -1) * -1)
        do = other.real * (other.imaginary * -1)
        di = other.imaginary * other.real

        bottom = df + dl + do + di
        new_real /= bottom
        new_imaginary /= bottom
        return self.formatter(new_real, new_imaginary)

    def _get_mod(self):
        return "{0:.2f}".format(
            ((self.real ** 2 + self.imaginary ** 2) ** 0.5))


# Tests

class TestComplexNumber(unittest.TestCase):

    def setUp(self):
        self.C = ComplexNumber("2 1".split())
        self.D = ComplexNumber("5 6".split())

    def test_add(self):
        result = self.C + self.D
        self.assertEqual(result, '7.00 + 7.00i')

    def test_sub(self):
        result = self.C - self.D
        self.assertEqual(result, '-3.00 - 5.00i')

    def test_mul(self):
        result = self.C * self.D
        self.assertEqual(result, '4.00 + 17.00i')

    def test_div(self):
        result = self.C / self.D
        self.assertEqual(result, '0.26 - 0.11i')

    def test_mod(self):
        c_result = self.C._get_mod()
        d_result = self.D._get_mod()
        self.assertEqual(c_result, '2.24')
        self.assertEqual(d_result, '7.81')

if __name__ == '__main__':
    unittest.main()
