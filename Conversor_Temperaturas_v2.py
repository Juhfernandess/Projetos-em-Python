# Funções para conversão de temperatura
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

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
    resultado = celsius_para_fahrenheit(temperatura)
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")
elif opcao == 2:
    resultado = celsius_para_kelvin(temperatura)
    print(f"A temperatura em Kelvin é: {resultado:.2f}K")
elif opcao == 3:
    resultado = fahrenheit_para_celsius(temperatura)
    print(f"A temperatura em Celsius é: {resultado:.2f}°C")
elif opcao == 4:
    resultado = fahrenheit_para_kelvin(temperatura)
    print(f"A temperatura em Kelvin é: {resultado:.2f}K")
elif opcao == 5:
    resultado = kelvin_para_celsius(temperatura)
    print(f"A temperatura em Celsius é: {resultado:.2f}°C")
elif opcao == 6:
    resultado = kelvin_para_fahrenheit(temperatura)
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")
else:
    print("Opção inválida.")
