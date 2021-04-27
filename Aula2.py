# print(2 + 2)
# print(2 - 2)
# print(2 * 2)
# print(2 / 2)
# print(2 // 2) #Divisão retornando int
# print(2 ** 3)
# print(10 % 3)
# print (5 * 2 + 3 * 2)
# print (5 * (2 + 3) * 2)

ano_atual = 2021
ano_fabricacao = 2003
km_total = 44410.0

# print(ano_atual)
# print(ano_fabricacao)
# print(km_total)

km_media = km_total / (ano_atual - ano_fabricacao)
# print (km_media)

ano_atual = 2021
ano_fabricacao = 2003
km_total = 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)

km_total += km_media
# print(km_total)

ano_atual, ano_fabricacao, km_total = 2021, 2003, 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)
# print(km_media)

# print(type(ano_atual))
# print(type(km_total))

zero_km = True
# print(type(zero_km))

nome = 'Jetta Variant'
# print(nome)
# print(type(nome))

carro = '''
    Nome
    Idade
    Nota
'''
# print(type(carro))

km = None
# print(km)
# print(type(km))

a = 10
b = 20
c = 'Python é '
d = 'legal'

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# print (a + b)
# print (c + d)

# print (c + a)

# print(str(a))
# print(type(str(a)))
#
# print(c + str(a))
#
# print(float(a))
# print(type(float(a)))

var = 3.1415
# print(int(var))
# print(type(int(var)))

ano_atual = 2021
ano_fabricacao = 2021

if (ano_atual == ano_fabricacao):
    print('Verdadeiro')
else:
    print('Falso')

# print('Olá, {}!'.format('Leandro'))
#
# print('Olá, {}! Esse é seu acesso de no. {}'.format('Leandro', 27))
# print('Olá, {nome}! Esse é seu acesso de no. {acessos}'.format(nome = 'Leandro', acessos = 27))

# f-Strings
# nome = 'Leandro'
# acessos = 27
# print(f'Olá, {nome}! Esse é seu acesso de no. {acessos}')

