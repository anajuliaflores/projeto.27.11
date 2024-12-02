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


'''
Primeiro importamos a biblioteca Numpy para que possamos usar as expressões numéricas contidas no código.
Depois criamos um array bidimensional (matriz) com 5 linhas representando os alunos e 4 colunas representando as provas.
Posteriormente fazemos uma lista da média dos alunos,
      colocamos media_alunos = notas.mean(axis=1)
                              chamamos a matriz notas e usamos o 'mean' que é uma função do numpy para calcular a média dos valores
                              e usamos o 'axis=1' para dizer que queremos que use os valores das colunas.
Depois usamos mais uma lista da médias das provas,
        colocamos media_provas = notas.mean(axis=0)
                            chamamos a matriz notas e usamos o 'mean' que é uma função de numpy para calcular a média dos valores
                            e usamos o 'axis=0' para dizer que queremos que use os valores das linhas.
Para finalizar colomos o print para apresentar o resultado chamando a media_alunos e a media_provas.
'''