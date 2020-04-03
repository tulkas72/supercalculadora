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

    def test_restar(self):
        sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica())
        self.assertEqual("0", sc.calcular("2 - 2"))

    def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
        sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica())
        self.assertEqual("6", sc.calcular("5 + 4 - 3"))
