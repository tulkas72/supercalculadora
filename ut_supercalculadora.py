import unittest
import supercalculadora


class TestsSupercalculadora(unittest.TestCase):
    def test_sumar_2_y_2(self):
        calc = supercalculadora.Supercalculadora()
        self.failUnlessEqual(4, calc.sumar(2, 2))  # deprecation warning


if __name__ == "__main__":
    unittest.main()
