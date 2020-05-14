import unittest
import test_calculadora
import test_expr_aritmetica
import test_supercalculadora
import calculadora
import expr_aritmetica

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_calculadora.TestCalculadora))
    suite.addTest(unittest.makeSuite(
        test_expr_aritmetica.TestsExprAritmetica))
    suite.addTest(unittest.makeSuite(
        test_supercalculadora.TestsSupercalculadora))
    unittest.TextTestRunner(verbosity=2).run(suite)
