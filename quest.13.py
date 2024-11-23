'''
Crie dois arrays 1D de tamanho 5. Eleve cada elemento do primeiro array ao
quadrado e subtraia o correspondente elemento do segundo array.
'''

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

resultado = array1**2 - array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Resultado:", resultado)
