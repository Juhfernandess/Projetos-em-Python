print("===== CAIXA ELETRÔNICO =====")
valor = int(input("Digite o valor a ser sacado: R$"))

# Inicialização das cédulas disponíveis
cedulas = [100,50, 20, 10, 1]

print("\nNotas entregues:")
for cedula in cedulas:
    quantidade = valor // cedula  # Calcula quantas notas dessa cédula são necessárias
    valor %= cedula  # Atualiza o valor restante a ser sacado
    
    if quantidade > 0:  # Apenas exibe se houver alguma nota dessa sendo entregue
        print(f"{quantidade} nota(s) de R${cedula}")

print("\nSaque finalizado!")
