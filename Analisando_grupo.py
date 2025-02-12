#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo,
#  qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Inicializando variáveis
soma_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

# Loop para ler os dados de 4 pessoas
for i in range(1, 5):
    print(f"\n--- {i}ª PESSOA ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    # Somando as idades para calcular a média
    soma_idade += idade

    # Verificando se é um homem e se é o mais velho
    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    # Contando mulheres com menos de 20 anos
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

# Calculando a média de idade
media_idade = soma_idade / 4

# Exibindo os resultados
print("\n===== RESULTADOS =====")
print(f"Média de idade do grupo: {media_idade:.1f} anos")
if homem_mais_velho:
    print(f"Homem mais velho: {homem_mais_velho} com {idade_homem_mais_velho} anos")
else:
    print("Não há homens no grupo.")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
