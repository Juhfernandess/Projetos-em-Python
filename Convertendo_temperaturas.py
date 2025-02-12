# Menu de opções
print("Escolha a conversão que deseja realizar:")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")

# Leitura da opção
opcao = int(input("Digite o número da opção desejada: "))

# Leitura da temperatura
if opcao == 1 or opcao == 2:
    temperatura = float(input("Digite a temperatura em Celsius: "))
elif opcao == 3 or opcao == 4:
    temperatura = float(input("Digite a temperatura em Fahrenheit: "))
else:
    temperatura = float(input("Digite a temperatura em Kelvin: "))

# Realizando a conversão com base na opção
if opcao == 1:
    # Celsius para Fahrenheit
    resultado = (temperatura * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")
elif opcao == 2:
    # Celsius para Kelvin
    resultado = temperatura + 273.15
    print(f"A temperatura em Kelvin é: {resultado:.2f}K")
elif opcao == 3:
    # Fahrenheit para Celsius
    resultado = (temperatura - 32) * 5/9
    print(f"A temperatura em Celsius é: {resultado:.2f}°C")
elif opcao == 4:
    # Fahrenheit para Kelvin
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"A temperatura em Kelvin é: {resultado:.2f}K")
elif opcao == 5:
    # Kelvin para Celsius
    resultado = temperatura - 273.15
    print(f"A temperatura em Celsius é: {resultado:.2f}°C")
elif opcao == 6:
    # Kelvin para Fahrenheit
    resultado = (temperatura - 273.15) * 9/5 + 32
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")
else:
    print("Opção inválida.")
