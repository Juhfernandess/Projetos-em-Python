#fa um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print("Digite a largura da parede em metros:")
largura = float(input())
print("Digite a altura da parede em metros:")
altura = float(input())

area = largura * altura
tinta_necessaria = area / 2

print(f"A área da parede é {area:.2f} metros quadrados.")
print(f"Você precisará de {tinta_necessaria:.2f} litros de tinta para pintá-la.")
