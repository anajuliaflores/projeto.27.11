'''
Crie um array de tamanho 15 contendo números inteiros aleatórios entre 0 e
100. Use máscaras para:
a. Selecionar todos os números pares.
b. Substituir os números ímpares por -1.
'''

import numpy as np

array = np.random.randint(0, 101, 15)

pares = array[array % 2 == 0]

array[array % 2 != 0] = -1

print(f"Array original: {array}")
print(f"Números pares: {pares}")
