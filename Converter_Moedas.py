print("Conversor de Moedas:")
print("1 - Real para Dólar")
print("2 - Real para Euro")
print("3 - Dólar para Real")
print("4 - Euro para Real")
print("5 - Dólar para Euro")
print("6 - Euro para Dólar")

opcao = input("Escolha a conversão desejada: ")
valor = float(input("Digite o valor: "))

taxa_dolar = 5.0  # Exemplo de taxa de câmbio

taxa_euro = 5.5  # Exemplo de taxa de câmbio

taxa_dolar_euro = 0.91  # Exemplo de taxa de câmbio

if opcao == '1':
    convertido = valor / taxa_dolar
    print(f"{valor} reais equivalem a {convertido:.2f} dólares.")
elif opcao == '2':
    convertido = valor / taxa_euro
    print(f"{valor} reais equivalem a {convertido:.2f} euros.")
elif opcao == '3':
    convertido = valor * taxa_dolar
    print(f"{valor} dólares equivalem a {convertido:.2f} reais.")
elif opcao == '4':
    convertido = valor * taxa_euro
    print(f"{valor} euros equivalem a {convertido:.2f} reais.")
elif opcao == '5':
    convertido = valor * taxa_dolar_euro
    print(f"{valor} dólares equivalem a {convertido:.2f} euros.")
elif opcao == '6':
    convertido = valor / taxa_dolar_euro
    print(f"{valor} euros equivalem a {convertido:.2f} dólares.")
else:
    print("Opção inválida!")
