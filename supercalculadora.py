import expr_aritmetica
import calculadora


class Supercalculadora:
    def __init__(self, parser):
        self.calc = calculadora.Calculadora()
        self.parser = parser

    def calcular(self, expresion):
        expr_descompuesta = self.parser.parse(expresion)
        res = 0
        for i in range(len(expr_descompuesta['Operadores'])):
            if i == 0:
                res = expr_descompuesta['Operandos'][0]
            if expr_descompuesta['Operadores'][i] == '+':
                res = self.calc.sumar(
                    res,
                    expr_descompuesta['Operandos'][i+1])
            elif expr_descompuesta['Operadores'][i] == '-':
                res = self.calc.restar(
                    res,
                    expr_descompuesta['Operandos'][i+1])

        return str(res)
