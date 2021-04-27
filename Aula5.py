import time
import numpy as np
# from numpy import arange

# print(np.arange(10))
# print(arange(10))

# km = np.array([100,2300,4897, 1500])
# print(km)
# print(type(km))
# print(km.dtype)

km = np.loadtxt(fname = 'data/carros-km.txt', dtype = int)
# print(km)
# print(km.dtype)

dados = [
['Rodas de liga', 'Travas Elétricas', 'Piloto Automático', 'Bancos de Couro', 'Ar Condicionado', 'Sensor de Estacionamento', 'Sensor Crepuscular', 'Sensor de Chuva'],
['Central Multimidia', 'Teto Panorâmico', 'Freios ABS', '4 X 4', 'Painel Digital', 'Piloto Automático', 'Bancos de Couro', 'Camera de Estacionamento'],
['Piloto Automático', 'Controle de Estabilidade', 'Sensor Crepuscular', 'Freios ABS', 'Cambio Automatico', 'Bancos de Couro', 'Central Multimidia', 'Vidros Eletricos']
]
# print(dados)

acessorios = np.array(dados)
# print(acessorios)
# print(acessorios.dtype)
# print(km.shape)
# print(acessorios.shape)

# np_array = np.arange(1000000)
# py_list = list(range(1000000))

# st = time.time()
# for _ in range(100):
#     np_array *= 2
# print("----%.2f----"%(time.time()-st))
#
# st = time.time()
# for _ in range(100):
#     py_list = [x * 2 for x in py_list]
# print("----%.2f----"%(time.time()-st))

km = [44410., 5712, 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]

# idade = 2021 - anos

km = np.array([44410., 5712, 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2021 - anos
# print(idade)

km_media = km / idade
# print(km_media)

dados = np.array([km, anos])
# print(dados)
# print(dados.shape)

# print(dados[0])
# print(dados[1])

km_media = dados[0] / (2021 - dados[1])
# print(km_media)

contador = np.arange(10)
# print(contador)

item = 6
index = item - 1
# print(contador[index])
# print(contador[-1])

# print(dados[1][2])
# print(dados[1, 2])

# print(contador[1:4])
# print(contador[1:8:2])
# print(contador[::2]) #Pares
# print(contador[1::2]) #Impares

# print(dados[:, 1: 4]) #Todas as linhas, colunas 1,2,3 (4 fica fora)
# print(dados[:, 1: 4][0]) #Na linha 0
# print(dados[:, 1: 3][0] / (2021 - dados[:, 1: 3][1])) #2 primeiras colunas da linha 0 dividido pelas da linha 1

# print(contador > 5)
# print(contador[contador > 5])
# print(contador[[False, False, False, False, False, False, True, True,  True,  True]])
#
# print(dados[1] > 2000)
# print(dados[:, dados[1] > 2000])