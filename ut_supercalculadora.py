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
        "añadido setup y teardown debajo"
        self.sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica())

    def tearDown(self):
        pass

    def test_sumar(self):
        self.assertEqual("4", self.sc.calcular("2 + 2"))

    def test_restar(self):
        self.assertEqual("0", self.sc.calcular("2 - 2"))

    def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
        self.assertEqual("6", self.sc.calcular("5 + 4 - 3"))

# añade función de simplificar
    def test_expresion_compleja_sin_parentesis_con_precedencia(self):
        self.assertEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))
        self.assertEqual("-1", self.sc.calcular("4 / 2 - 3"))
        self.assertEqual("1", self.sc.calcular("4 / 2 - 3 + 1 + 6 / 3 - 1"))
        self.assertEqual(
            "-8", self.sc.calcular("4 / -2 + 3 + -1 + -6 / -3 - 10"))
        self.assertEqual("9", self.sc.calcular("5 + 4 * 2 / 2"))  # n

        # prueba para comprobar si la división lanza una excepción si el resultado no es exacto
        self.assertEqual("11", self.sc.calcular("4 - -3 * 2 / 3 + 5"))  # n
