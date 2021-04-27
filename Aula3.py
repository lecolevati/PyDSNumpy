acessorios = ['Rodas de liga', 'Travas Elétricas', 'Piloto Automático', 'Bancos de Couro', 'Ar Condicionado', 'Sensor de Estacionamento', 'Sensor Crepúsculo', 'Sensor de Chuva']
# print(acessorios)
# print(type(acessorios))

carro1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas Elétricas', 'Piloto Automático'], 88078.64]
carro2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Sensor Multimidia', 'Teto panorâmico', 'Freio ABS'], 106161.94]

# print(carro1)
# print(type(carro1))
# print(carro2)
# print(type(carro2))

carros = [carro1, carro2]
# print(carros)
# print(type(carros))

# print('Rodas de liga' in carro1)
# print('Rodas de liga' not in acessorios)
# print('4 x 4' in acessorios)
# print('4 x 4' not in acessorios)

A = ['Rodas de liga', 'Travas Elétricas', 'Piloto Automático', 'Bancos de Couro']
B = ['Ar Condicionado', 'Sensor de Estacionamento', 'Sensor Crepúsculo', 'Sensor de Chuva']
# print (A + B)

# print(len(acessorios))

# print(acessorios[0])
# print(acessorios[1])
# print(acessorios[-1]) #Último item da lista
# print(acessorios[-2]) #Penultimo item da lista

# print(carros[0])
# print(carros[0][-2][1])

# print(acessorios[2:5]) #primeiro elemento entra na lista, o 2o não entra
# print(acessorios[2:6]) #primeiro elemento entra na lista, o 2o não entra
# print(acessorios[2:]) #todos a  partir de 2
# print(acessorios[:5]) #todos até o 4 (5 não entra)

# acessorios.sort()
# print(acessorios)

# acessorios.append("4 X 4")
# print(acessorios)

# acessorios.pop()
# print(acessorios)
#
# acessorios.pop(3)
# print(acessorios)

# Copia por valor e não por referência
acessorios2 = acessorios.copy()
# print(acessorios2)

acessorios2.append("4 X 4")
# print(acessorios2)
# print(acessorios)

# acessorios2 = acessorios[:] #É equivalente ao copy

# for item in acessorios:
#     print(item)

# print(list(range(10)))

# for i in range(10):
#     print(i ** 2)

# quadrado = []
# for i in range(10):
#     quadrado.append(i ** 2)
#
# print(quadrado)

# print('x')
# print([i ** 2 for i in range(10)]) #semelhante ao for

dados = [
['Rodas de liga', 'Travas Elétricas', 'Piloto Automático', 'Bancos de Couro', 'Ar Condicionado', 'Sensor de Estacionamento', 'Sensor Crepuscular', 'Sensor de Chuva'],
['Central Multimidia', 'Teto Panorâmico', 'Freios ABS', '4 X 4', 'Painel Digital', 'Piloto Automático', 'Bancos de Couro', 'Camera de Estacionamento'],
['Piloto Automático', 'Controle de Estabilidade', 'Sensor Crepuscular', 'Freios ABS', 'Cambio Automatico', 'Bancos de Couro', 'Central Multimidia', 'Vidros Eletricos']
]
# print(dados)

# for lista in dados:
#     print(lista)

# for lista in dados:
#     for item in lista:
#         print(item)

acess = []
for lista in dados:
    for item in lista:
        acess.append(item)
# print(acess)
set_acess = set(acess)
acess_sem_dupl = list(set_acess)
# print(acess_sem_dupl)

#De outra forma:
# print(list(set([item for lista in dados for item in lista])))

