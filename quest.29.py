'''
Crie um sinal simulado usando y=sin(2πfx), onde f=5 e x varia de 0 a 1 com
100 amostras. Use numpy.fft para calcular a Transformada de Fourier
desse sinal.
'''

import numpy as np
import matplotlib.pyplot as plt

f = 5
x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * f * x)

Y = np.fft.fft(y)
frequencias = np.fft.fftfreq(len(x), x[1] - x[0])

plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title("Sinal Original")

plt.subplot(2, 1, 2)
plt.plot(frequencias, np.abs(Y))
plt.title("Magnitude da Transformada de Fourier")

plt.tight_layout()
plt.show()
