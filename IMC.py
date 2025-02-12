# Leitura do peso e altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do IMC e classificação
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Status: Abaixo do Peso ❌")
elif 18.5 <= imc < 25:
    print("Status: Peso Ideal ✅")
elif 25 <= imc < 30:
    print("Status: Sobrepeso ⚠️")
elif 30 <= imc < 40:
    print("Status: Obesidade 🚨")
else:
    print("Status: Obesidade Mórbida 🔴")
