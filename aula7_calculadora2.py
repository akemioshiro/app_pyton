class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor1, valor2):
        return valor1 + valor2

    def subtracao (self, valor1, valor2):
        return valor1 - valor2

    def multiplicacao(self, valor1, valor2):
        return valor1 * valor2

    def divisao(self, valor1, valor2):
        return valor1 / valor2


calculadora  = Calculadora()
print(calculadora.soma(1,5))
print(calculadora.multiplicacao(10,10))