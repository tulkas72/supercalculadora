import unittest
import supercalculadora
import expr_aritmetica
import test_calculadora
import test_expr_aritmetica
import validador_expr_aritmetica
from mox3 import mox


class TestsSupercalculadora(unittest.TestCase):
    def setUp(self):
        "añadido setup y teardown debajo"
        self.sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica(), validador_expr_aritmetica.ValidadorExprAritmetica())

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

    # refact y mock
    def test_expresion_compleja_todas_operaciones_sin_parentesis(self):
        # prueba para comprobar si la división lanza una excepción si el resultado no es exacto
        self.assertEqual("11", self.sc.calcular("4 - -3 * 2 / 3 + 5"))  # n

    def test_validador_expresión_invalida_stub(self):
        """vamos a crear una última prueba con un stub y vamos a cambiar nuestro
         diseño en base a esto sin necesidad de implementar nada(o casi nada).
         Mocks, stubs y similares son herramientas que nos permiten simular ciertos
         comportamientos, herramientas, o funciones que aún no están disponibles, pero
         nos hacen falta para probar lo que tenemos hecho."""
        # falla en primera instancia, no hay clase Validador y Supercalculadora sólo recibe un parámetro
        validador_stub = validador_expr_aritmetica.ValidadorExprAritmetica()
        validar_mock = mox.Mox()
        validar_mock.StubOutWithMock(validador_stub, 'validar')
        validador_stub.validar("2 ^ 3").AndReturn(False)
        validar_mock.ReplayAll()
        sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica(),    validador_stub)
        self.failUnlessRaises(SyntaxError, sc.calcular, "2 ^ 3")
        validar_mock.UnsetStubs()
        validar_mock.VerifyAll()
