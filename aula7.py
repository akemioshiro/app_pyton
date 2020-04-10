class Calculadora:
    def __init__(self, num1, num2):
        self.valor1 = num1
        self.valor2 = num2

    def soma(self):
        return self.valor1 + self.valor2

    def subtracao (self):
        return self.valor1 - self.valor2

    def multiplicacao(self):
        return self.valor1 * self.valor2

    def divisao(self):
        return self.valor1 / self.valor2


calculadora  = Calculadora(10,2)
print(calculadora.valor1)
print(calculadora.soma())
print(calculadora.multiplicacao())