class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def dividir(self, a, b):
        if b == 0:
            return ZeroDivisionError
        if a % b != 0:
            return ValueError
        else:
            return a / b  # En Python 2.x esto funciona sin problemas, pero en Python 3, no. ¿Sabes arreglarlo?
