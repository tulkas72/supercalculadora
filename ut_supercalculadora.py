import unittest
import supercalculadora
import expr_aritmetica
import ut_calculadora
import ut_expr_aritmetica


class TestsSupercalculadora(unittest.TestCase):
    def test_sumar(self):
        sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica())
        self.assertEqual("4", sc.calcular("2 + 2"))
