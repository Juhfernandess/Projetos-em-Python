#crieprograma que leia o nome completo de uma pessoa e mostre:
#  O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

# Leitura do nome
nome_completo = input("Digite o nome completo: ")

# Exibindo o nome em maiúsculas e minúsculas
print(f"O nome em maiúsculas: {nome_completo.upper()}")
print(f"O nome em minúsculas: {nome_completo.lower()}")

# Contando o total de letras (sem considerar espaços)
nome_sem_espacos = nome_completo.replace(" ", "")
total_letras = len(nome_sem_espacos)
print(f"Total de letras (sem considerar espaços): {total_letras}")

# Contando o número de letras do primeiro nome
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)
print(f"Quantidade de letras do primeiro nome: {letras_primeiro_nome}")
