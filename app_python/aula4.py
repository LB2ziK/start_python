a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('voce digitou errado. primeiro bimestrre'))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('voce digitou errado. segundo bimestre'))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('voce digitou errado. terceiro bimestre'))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('voce digitou errado. quarto bimestre'))
media = (a + b + c + d) / 4
print('media: {}'.format(media))


# nota = int(input('entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida. entre com a nota correta: '))
# print(nota)



# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('entre com valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)



# a = int(input('Entre com o numero: '))
#
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
#
# if div == 2:
#     print('numero {} é primo'.format(a))
# else:
#     print('numero {} nao é primo'.format(a))
