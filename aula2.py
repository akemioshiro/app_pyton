a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))


soma  = a + b
subtracao = a -b
divisao = a / b
multiplicacao  = a * b
resto = a % b
# comentários
print (type(soma))
print(soma)
soma = str(soma)
print(type(soma))
print(subtracao)
x = '1'
soma2 = int(x) + int(soma)
print(soma2)

print('soma: {}, subtracao: {}, multiplicacao: {}'.format(soma, subtracao, multiplicacao))

resultado = ('Soma: {soma} '
      '\nSubtração: {subtracao} '
      '\nMultiplicação: {multiplicacao}'
      .format(soma = 1,subtracao = 3,multiplicacao = 5))

print(resultado)


