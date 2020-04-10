contador_letras = lambda lista:[len(x) for x in lista]

lista_animal = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animal))

soma =  lambda a,b: a+b
subtracao = lambda a,b : a-b
print(soma(5,10))
print(subtracao(7,3))

calculadora = {
    'soma': lambda a,b : a+b,
    'subtracao': lambda  a,b : a-b,
    'multiplicacao': lambda  a,b : a*b,
    'divisao': lambda a,b: a/b
}

print(type(calculadora))
soma = calculadora['soma']
# soma = lambda a,b : a+b
multiplicaco = calculadora['multiplicacao']

print(soma(10,9))
print('a multiplicacao é {}' .format(multiplicaco(91,7)))