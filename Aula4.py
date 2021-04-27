#1o item - Nome
#2o item - Ano
#3o item - Zero Km ?
dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Journey', 2019, False],
    ['Carens', 2011, False],
]
# print(dados)

# zero_km_y = []
# for lista in dados:
#     if(lista[2] == True):
#         zero_km_y.append(lista)

# print(zero_km_y)

# zero_km_n = []
# for lista in dados:
#     if(lista[2] == False):
#         zero_km_n.append(lista)

# print(zero_km_n)

# list comprehensions
# print([lista for lista in dados if lista[2] == True])
# print([lista for lista in dados if lista[2] == False])

zero_km_y = []
zero_km_n = []
for lista in dados:
    if(lista[2] == False):
        zero_km_n.append(lista)
    else:
        zero_km_y.append(lista)

# print(zero_km_n)
# print(zero_km_y)

A, B, C = [], [], []

# for lista in dados:
#     if (lista[1] <= 2000):
#         A.append(lista)
#     elif (lista[1] >= 2000 and lista[1] <= 2010):
#         B.append(lista)
#     else:
#         C.append(lista)

# print(A)
# print(B)
# print(C)

#Python aceita esse teste do elif
for lista in dados:
    if (lista[1] <= 2000):
        A.append(lista)
    elif (2000 < lista[1] <= 2010):
        B.append(lista)
    else:
        C.append(lista)

print(A)
print(B)
print(C)
