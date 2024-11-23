'''
Crie um array bidimensional representando notas de 5 alunos em 4 provas.
Calcule a média de cada aluno e a média de cada prova.
'''

import numpy as np

notas = np.array([
    [8.0, 7.5, 9.0, 6.5],
    [7.0, 8.0, 8.5, 9.0],
    [6.5, 7.0, 7.5, 8.0],
    [9.0, 8.5, 8.0, 7.5],
    [7.5, 6.5, 9.0, 8.5]
])

media_alunos = notas.mean(axis=1) 
media_provas = notas.mean(axis=0)  

print("Média de cada aluno:", media_alunos)
print("Média de cada prova:", media_provas)
