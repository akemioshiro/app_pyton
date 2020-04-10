from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, test



if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(1,36)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    print('total letras: {}' .format(contador_letras(lista)))

    print(test())