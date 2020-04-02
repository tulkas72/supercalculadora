
import unittest
import ut_calculadora
import ut_expr_aritmetica
import calculadora
import expr_aritmetica


class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        sc = calculadora.Calculadora(
            expr_aritmetica.ExprAritmetica())
        self.assertEqual("4", sc.calcular("2 + 2"))


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ut_calculadora.TestCalculadora))
    suite.addTest(unittest.makeSuite(ut_expr_aritmetica.TestsExprAritmetica))
    suite.addTest(unittest.makeSuite(TestCalculadora))
    unittest.TextTestRunner(verbosity=3).run(suite)
