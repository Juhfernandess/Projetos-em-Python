#: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#módulo para sortear
import random 

# Leitura dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Colocando os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteando um aluno
escolhido = random.choice(alunos)

# Exibição do nome do aluno escolhido
print(f"O aluno escolhido para apagar o quadro é: {escolhido}")
