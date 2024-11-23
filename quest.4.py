'''
Crie um array de 20 números aleatórios entre 0 e 1. Calcule a média, o
desvio padrão, o valor máximo e o mínimo desse array.
'''

import numpy as np

array = np.random.rand(20)

media = np.mean(array)
desvio_padrao = np.std(array)
maximo = np.max(array)
minimo = np.min(array)

print(f"Média: {media:.4f}")
print(f"Desvio Padrão: {desvio_padrao:.4f}")
print(f"Máximo: {maximo:.4f}")
print(f"Mínimo: {minimo:.4f}")
