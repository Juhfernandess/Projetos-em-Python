#inserindo a frase
frase = input("Digite uma frase: ").strip().lower()

# Transformando em uma única string
frase_sem_espacos = frase.replace(" ", "")

# Invertendo a frase
frase_invertida = frase_sem_espacos[::-1]

# Verificando se é um palíndromo
if frase_sem_espacos == frase_invertida:
    print("A frase é um PALÍNDROMO! ")
else:
    print("A frase NÃO é um palíndromo. ")
