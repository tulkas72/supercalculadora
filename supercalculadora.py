import expr_aritmetica
import calculadora


class Supercalculadora:
    def __init__(self, parser):
        self.calc = calculadora.Calculadora()
        self.parser = parser

    def calcular(self, expresion):
        expr_descompuesta = self.parser.parse(expresion)
        try:
            i = expr_descompuesta['Operadores'].index('/')
            res_intermedio = self.calc.dividir(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
            expr_descompuesta = {'Operandos':
                                 [expr_descompuesta['Operandos'][0],
                                  res_intermedio,
                                  expr_descompuesta['Operandos'][3]],
                                 'Operadores':
                                 [expr_descompuesta['Operadores'][0],
                                  expr_descompuesta['Operadores'][2]]}
        except ValueError:
            pass

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

# 1    # def simplificar(self, expr_descompuesta):
# 1    #     expr_simplificada = {}
# 1    #     try:
# 1    #         i = expr_descompuesta['Operadores'].index('/')
# 1    #         res_intermedio = self.calc.dividir(
# 1    #             expr_descompuesta['Operandos'][i],
# 1    #             expr_descompuesta['Operandos'][i + 1])
# 1    #         expr_simplificada = {'Operandos':
# 1    #                              [expr_descompuesta['Operandos'][0],
# 1    #                               res_intermedio,
# 1    #                               expr_descompuesta['Operandos'][3]],
# 1    #                              'Operadores':
# 1    #                              [expr_descompuesta['Operadores'][0],
# 1    #                               expr_descompuesta['Operadores'][2]]}
# 1    #     except ValueError:
# 1    #         expr_simplificada = expr_descompuesta
# 1
# 1    #     return expr_simplificada

# 2    def simplificar(self, expr_descompuesta):
# 2        "simplifcar, primera modificación"
# 2        expr_simplificada = {}
# 2        try:
# 2            i = expr_descompuesta['Operadores'].index('/')
# 2            res_intermedio = self.calc.dividir(
# 2                expr_descompuesta['Operandos'][i],
# 2                expr_descompuesta['Operandos'][i + 1])
# 2
# 2            expr_simplificada = expr_descompuesta
# 2            expr_simplificada['Operadores'].pop(i)
# 2            expr_simplificada['Operandos'].pop(i)
# 2            expr_simplificada['Operandos'].pop(i)
# 2            expr_simplificada['Operandos'].insert(i, res_intermedio)
# 2        except ValueError:
# 2            expr_simplificada = expr_descompuesta
# 2
# 2        return expr_simplificada

# 1    def calcular(self, expresion):
# 1        expr_simplificada = self.simplificar(self.parser.parse(expresion))
# 1        res = 0
# 1        for i in range(len(expr_simplificada['Operadores'])):
# 1            if i == 0:
# 1                res = expr_simplificada['Operandos'][0]
# 1            if expr_simplificada['Operadores'][i] == '+':
# 1                res = self.calc.sumar(
# 1                    res,
# 1                    expr_simplificada['Operandos'][i+1])
# 1            elif expr_simplificada['Operadores'][i] == '-':
# 1                res = self.calc.restar(
# 1                    res,
# 1                    expr_simplificada['Operandos'][i+1])
# 1
# 1        return str(res)

# 3    def __operar__(self, expr_descompuesta):
# 3        i = None
# 3        res_intermedio = 0
# 3        if '/' in expr_descompuesta['Operadores']:
# 3            i = expr_descompuesta['Operadores'].index('/')
# 3            res_intermedio = self.calc.dividir(
# 3                expr_descompuesta['Operandos'][i],
# 3                expr_descompuesta['Operandos'][i + 1])
# 3        elif '-' in expr_descompuesta['Operadores']:
# 3            i = expr_descompuesta['Operadores'].index('-')
# 3            res_intermedio = self.calc.restar(
# 3                expr_descompuesta['Operandos'][i],
# 3                expr_descompuesta['Operandos'][i + 1])
# 3        elif '+' in expr_descompuesta['Operadores']:
# 3            i = expr_descompuesta['Operadores'].index('+')
# 3            res_intermedio = self.calc.sumar(
# 3                expr_descompuesta['Operandos'][i],
# 3                expr_descompuesta['Operandos'][i + 1])
# 3        else:
# 3            # Es un error, tenemos que decidir que hacer en los test
# 3            # siguientes
# 3            # Forzamos el error para que no haya problemas luego
# 3            assert False
# 3        return (i, res_intermedio)
# 3
# 3    def __simplificar__(self, expr_descompuesta):
# 3        if expr_descompuesta['Operadores'] == []:
# 3            return expr_descompuesta
# 3
# 3        (i, res_intermedio) = self.__operar__(expr_descompuesta)
# 3        expr_simplificada = expr_descompuesta
# 3        expr_simplificada['Operadores'].pop(i)
# 3        expr_simplificada['Operandos'].pop(i)
# 3        expr_simplificada['Operandos'].pop(i)
# 3        expr_simplificada['Operandos'].insert(i, res_intermedio)
# 3
# 3        return self.__simplificar__(expr_simplificada)
# 3
# 3    def calcular(self, expresion):
# 3        return str(self.__simplificar__(
# 3            self.parser.parse(expresion))['Operandos'][0])
