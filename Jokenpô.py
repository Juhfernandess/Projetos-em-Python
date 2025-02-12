import random

# Opções disponíveis
opcoes = ["pedra", "papel", "tesoura"]

# Usuário escolhe sua jogada
print("--------JOKENPÔ----------")
usuario = input("Escolha pedra, papel ou tesoura: ").strip().lower()

# Verifica se a escolha do usuário é válida
if usuario not in opcoes:
    print("Escolha inválida! Tente novamente.")
else:
    # Computador escolhe aleatoriamente
    computador = random.choice(opcoes)

    # Exibe as escolhas
    print(f"\nVocê escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")

    # Determina o resultado
    if usuario == computador:
        print("Empate! 🤝")
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
         (usuario == "tesoura" and computador == "papel"):
        print("Você venceu! Meus parabéns!")
    else:
        print("Você perdeu! Jogue mais uma vez!")
