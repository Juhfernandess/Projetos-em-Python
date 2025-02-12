import random

# Computador escolhe um número aleatório entre 0 e 5
numero_secreto = random.randint(0, 5)

# Usuário tenta adivinhar o número
palpite = int(input("Tente adivinhar o número entre 0 e 5 que o computador escolheu: "))

# Verifica se o usuário acertou
if palpite == numero_secreto:
    print("Parabéns! Você acertou! ")
else:
    print(f"Que pena! Você errou. O número correto era {numero_secreto}.")
