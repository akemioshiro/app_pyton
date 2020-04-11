lista = [1, 10]

try:
    divisao = 10 / 1
    numero = lista [1]
    x = a
except ZeroDivisionError:
    print('Divisão por zero')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('Erro desconhecido: {} '.format(ex))