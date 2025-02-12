#aça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

import math

# Leitura dos comprimentos dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# teorema de Pitágoras
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Exibição do comprimento da hipotenusa
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")

