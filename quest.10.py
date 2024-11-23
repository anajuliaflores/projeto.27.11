'''
Gere um conjunto de dados simulando as alturas (em cm) de 100 pessoas,
usando uma distribuição normal com média 170 e desvio padrão 10. Depois
calcule:
a. O percentil 25, 50 (mediana) e 75.
b. A quantidade de pessoas com altura acima de 180 cm.
c. Plote um histograma dos dados usando Matplotlib (não precisa
detalhar o código da plotagem).
'''

import numpy as np
import matplotlib.pyplot as plt

alturas = np.random.normal(170, 10, 100)

percentis = np.percentile(alturas, [25, 50, 75])
acima_180 = np.sum(alturas > 180)

print(f"Percentil 25: {percentis[0]:.2f} cm")
print(f"Percentil 50 (mediana): {percentis[1]:.2f} cm")
print(f"Percentil 75: {percentis[2]:.2f} cm")
print(f"Quantidade de pessoas com altura acima de 180 cm: {acima_180}")

plt.hist(alturas, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title("Distribuição de Alturas")
plt.xlabel("Altura (cm)")
plt.ylabel("Frequência")
plt.show()
