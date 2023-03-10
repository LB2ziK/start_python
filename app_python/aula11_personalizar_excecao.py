class Error(Exception):
    pass

class ImputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('entre cm o valor de 0 a 10: '))
        print(x)
        if x > 10:
            raise ImputError('nota nao pode ser maior que 10')
        elif x < 0:
            raise ImputError('nota nao pode ser menor que 0')
        break
    except ValueError:
        print('valor invalido, deve-se usar apenas numeros.')
    except ImputError as ex:
        print(ex)