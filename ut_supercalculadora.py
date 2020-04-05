import unittest
import supercalculadora
import expr_aritmetica
import ut_calculadora
import ut_expr_aritmetica


# class TestsSupercalculadora(unittest.TestCase):
#     def test_sumar(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("4", sc.calcular("2 + 2"))

#     def test_restar(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("0", sc.calcular("2 - 2"))

#     def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("6", sc.calcular("5 + 4 - 3"))

#     def test_expresion_compleja_sin_parentesis_con_precedencia(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("3", sc.calcular("5 + 4 / 2 - 4"))


class TestsSupercalculadora(unittest.TestCase):
    def setUp(self):
        self.sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica())

    def tearDown(self):
        pass

    def test_sumar(self):
        self.failUnlessEqual("4", self.sc.calcular("2 + 2"))

    def test_restar(self):
        self.failUnlessEqual("0", self.sc.calcular("2 - 2"))

    def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
        self.failUnlessEqual("6", self.sc.calcular("5 + 4 - 3"))

# añade función de simplificar
# 1    def test_expresion_compleja_sin_parentesis_con_precedencia(self):
# 1        self.failUnlessEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))

# modifica función simplificar
# 2    def test_expresion_compleja_sin_parentesis_con_precedencia(self):
# 2        self.failUnlessEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))
# 3        self.failUnlessEqual("-1", self.sc.calcular("4 / 2 - 3"))
