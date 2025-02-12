print("Digite um número inteiro para ver sua tabuada:")
num = int(input())
print(f"Tabuada de {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
