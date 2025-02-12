# mesmo professor do desafio anterior tear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

# Leitura dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Colocando os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteando a ordem dos alunos
random.shuffle(alunos)

# Exibição da ordem sorteada
print("A ordem de apresentação dos trabalhos é:")
for i, aluno in enumerate(alunos, 1):
    print(f"{i} - {aluno}")
