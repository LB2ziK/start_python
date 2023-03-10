
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('nao e possivel realizar divisao por 0')
except ArithmeticError:
    print('houve um erro ao realizar uma operacao aritimetica')
except IndexError:
    print('erro ao acessar um indice da lista')
except Exception as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('executa quando nao ocorre exceção')
finally:
    print('sempre executa')
    print('fechando arquivo')
    arquivo.close()
