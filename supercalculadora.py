"""Super Calculadora. Módulo para hacer cálculos con expresiones enteras.
Este módulo recibe una cadena con una expresión aritmética "entera" y realiza los
cálculos de esa expresión. 
Raises:
    SyntaxError: [description]

Returns:
    [type]: [description]
Todo:
    * En operar hay que decidir qué hacer cuando se pasa un operador no reconocido
    
.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html    
"""
import expr_aritmetica
import calculadora
import validador_expr_aritmetica


class Supercalculadora:
    """[summary]
    """
    def __init__(self, parser, validador):  # añadido parámetro validador
        """[summary]

        Args:
            parser ([type]): [description]
            validador ([type]): [description]
        """
        self.calc = calculadora.Calculadora()
        self.parser = parser
        self.validador = validador

    def __operar__(self, expr_descompuesta):
        """[summary]

        Args:
            expr_descompuesta ([type]): [description]

        Returns:
            [type]: [description]
        """
        i = None
        res_intermedio = 0
        # intercambiar / y * por el error de la división
        if '*' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('*')
            res_intermedio = self.calc.multiplicar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        elif '/' in expr_descompuesta['Operadores']:  # n
            i = expr_descompuesta['Operadores'].index('/')  # n
            res_intermedio = self.calc.dividir(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])  # n
        elif '-' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('-')
            res_intermedio = self.calc.restar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        elif '+' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('+')
            res_intermedio = self.calc.sumar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        else:
            # Es un error, tenemos que decidir que hacer en los test
            # siguientes
            # Forzamos el error para que no haya problemas luego
            assert False
        return (i, res_intermedio)

    def __simplificar__(self, expr_descompuesta):
        """[summary]

        Args:
            expr_descompuesta ([type]): [description]

        Returns:
            [type]: [description]
        """
        if expr_descompuesta['Operadores'] == []:
            return expr_descompuesta

        (i, res_intermedio) = self.__operar__(expr_descompuesta)
        expr_simplificada = expr_descompuesta
        expr_simplificada['Operadores'].pop(i)
        expr_simplificada['Operandos'].pop(i)
        expr_simplificada['Operandos'].pop(i)
        expr_simplificada['Operandos'].insert(i, res_intermedio)

        return self.__simplificar__(expr_simplificada)

    def calcular(self, expresion):
        """[summary]

        Args:
            expresion ([type]): [description]

        Raises:
            SyntaxError: [description]

        Returns:
            [type]: [description]
        """
        if not self.validador.validar(expresion):  # añadido para mock
            raise SyntaxError("La expresion no es valida")

        return str(self.__simplificar__(
            self.parser.parse(expresion))['Operandos'][0])
