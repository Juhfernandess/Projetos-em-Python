import math 

angulo = float(input("Digite o valor do ângulo em graus: "))

# Convertendo o ângulo de graus para radianos
angulo_radiano = math.radians(angulo)

# Cálculo do seno, cosseno e tangente
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

print(f"O seno de {angulo}° é: {seno:.2f}")
print(f"O cosseno de {angulo}° é: {cosseno:.2f}")
print(f"A tangente de {angulo}° é: {tangente:.2f}")
