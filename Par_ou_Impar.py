import random

vitorias = 0  # Contador de vitórias consecutivas

print("===== JOGO DO PAR OU ÍMPAR =====")
print("Vamos ver se pode me vencer hehehe!")

while True:
    # Escolha do usuário
    jogador_numero = int(input("\nDigite um número jogador: "))
    jogador_escolha = input("Par ou Ímpar? (P/I): ").strip().upper()

    # Escolha e jogada do computador
    computador_numero = random.randint(0, 10)
    soma = jogador_numero + computador_numero
    resultado = "PAR" if soma % 2 == 0 else "ÍMPAR"

    # Exibir as jogadas
    print(f"\nVocê jogou {jogador_numero} e o computador jogou {computador_numero}.")
    print(f"Total: {soma} → {resultado}")

    # Verifica se o jogador ganhou ou perdeu
    if (jogador_escolha == "P" and resultado == "PAR") or (jogador_escolha == "I" and resultado == "ÍMPAR"):
        print("Você VENCEU! Aff, sorte de principiante! ")
        vitorias += 1
    else:
        print("Você PERDEU!Sou mesmo muito bom haha, mas pode jogar mais uma vez!")
        break  # Sai do loop se perder

print(f"\nFim de jogo! Você venceu {vitorias} vez(es) consecutivas.")
