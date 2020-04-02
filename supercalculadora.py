import expr_aritmetica
import calculadora


class Supercalculadora:
    def __init__(self, parser):
        self.calc = calculadora.Calculadora()
        self.parser = parser

    def calcular(self, expresion):
        expr_descompuesta = self.parser.parse(expresion)
        if expr_descompuesta['Operadores'][0] == '+':
            return str(self.calc.sumar(
                expr_descompuesta['Operandos'][0],
                expr_descompuesta['Operandos'][1]))
