import numpy as np

km = np.loadtxt('data/carros-km.txt')
# print(km)
anos = np.loadtxt('data/carros-anos.txt', dtype = int)
# print(anos)

km_media = km / (2021 - anos)
print(km_media)
print((type(km_media)))