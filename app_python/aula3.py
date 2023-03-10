a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('voce digitou errado. primeiro bimestrre'))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('voce digitou errado. segundo bimestre'))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('voce digitou errado. terceiro bimestre'))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('voce digitou errado. quarto bimestre'))
media = (a + b + c + d) / 4
print('media: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print ('media: {}'.format(media))
# else:
#     print('foi informado uma nota errada')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('foi registrado um numero par')
# else:
#     print('nenhum numero par foi digitado')



# a = int(input('Primeiro valor: '))
# b = int(input('Segundo Valo1r: '))
# c = int(input('Terceiro Valor: '))
# if a > b and a > c:
#     print('O maior numero é {}:'.format(a))
# elif b > a and b > c:
#     print('O maior numero é {}'.format(b))
# else:
#     print('O maior numero é {}'.format(c))
# print('final do programa')