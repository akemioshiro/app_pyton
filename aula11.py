lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista [1]
    x = a
except ZeroDivisionError:
    print('Divisão por zero')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('Erro desconhecido: {} '.format(ex))
else:
    print('executa quando não ocorre exceção')
finally:
    print('sempre executa')
    arquivo.close()
