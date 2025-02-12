# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Leitura do número
numero = int(input("Digite um número de 0 a 9999: "))

# Garantindo que o número esteja dentro do intervalo
if 0 <= numero <= 9999:
    # Extraindo os dígitos
    milhar = numero // 1000
    centena = (numero // 100) % 10
    dezena = (numero // 10) % 10
    unidade = numero % 10

    # Exibindo os dígitos
    print(f"Milhar: {milhar}")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")
else:
    print("Número fora do intervalo de 0 a 9999.")
