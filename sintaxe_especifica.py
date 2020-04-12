#13.1	LIST	COMPREHENSIONS
numbers_times = [ i for i in range(5)]
print(numbers_times)
pares = [i for i in range(10) if i%2==0]
print(pares)
lista_aninhada = [(i,j) for i in range(3) for j in range(2)]
print(lista_aninhada)

message =  'O nome do aluno é {nome}'.format(nome='Patricia')
print(message)

# função enumerate
impostos = ['MEI', 'Simples']
for i,imposto in enumerate(impostos):
    print(i, imposto)
