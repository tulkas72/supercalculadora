import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = calculadora.Calculadora()

    def tearDown(self):
        pass

    def test_sumar_2_y_2(self):
        self.assertEqual(4, self.calc.sumar(2, 2))

    def test_sumar_5_y_7(self):
        self.assertEqual(12, self.calc.sumar(5, 7))

    def test_sumar_propiedad_conmutativa(self):
        self.assertEqual(self.calc.sumar(5, 7),
                         self.calc.sumar(7, 5))

    def test_restar_5_y_3(self):
        self.assertEqual(2, self.calc.restar(5, 3))

    def test_restar_2_y_3(self):
        self.assertEqual(-1, self.calc.restar(2, 3))

    def test_restar_no_propiedad_conmutativa(self):
        self.assertNotEqual(self.calc.restar(5, 3),
                            self.calc.restar(3, 5))
