class Calculadora:
    def sumar(self, a:int, b:int)->int:
        """Suma de dos enteros

        :param a: primer sumando
        :type a: int
        :param b: segundo sumando
        :type b: int
        :return: suma
        :rtype: int

        """
        return a + b

    def restar(self, a:int, b:int)->int:
        """Resta de dos enteros

        :param a: minuendo
        :type a: int
        :param b: sustraendo
        :type b: int
        :return: diferencia
        :rtype: int

        """
        return a - b

    def multiplicar(self, a:int, b:int)->int:  # n
        """Multiplicación de dos enteros

        :param a: primer factor
        :type a:  int
        :param b: segundo factor
        :type b: int
        :return: factor
        :rtype: int

        """
        return a * b

    def dividir(self, a:int, b:int)->int:
        """Realiza la división entera de a entre b.

        .. warning:: Sólo si la división es exacta.
        .. note::
            * Si no es exacta devuelve ValueError.
            * Si el divisor es cero(0) devolvemos *ZeroDivisionError*
            * Originalmente hecho en Python 2 utilizando el operador
              "/" que, en Python 2 devuelve la división entera si los
              dos operandos son enteros, se ha cambiado a "//"
              operador específico para realizar la división entera.

        :param a: dividendo
        :type a: int
        :param b: divisor
        :type b: int
        :return: cociente
        :rtype: int

        :example:

        >>> import calculadora
        >>> ca = calculadora.Calculadora()
        >>> print(ca.dividir(4,2))

        """

        if b == 0:
            return ZeroDivisionError

        if a % b != 0:
            return ValueError
        else:
            return a // b  # En Python 2.x esto funciona sin problemas, pero en Python 3, no. ¿Sabes arreglarlo?
