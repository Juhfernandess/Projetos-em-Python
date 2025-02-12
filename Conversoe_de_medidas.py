print("Selecione o tipo de conversão:")
print("1 - km para hm")
print("2 - hm para dam")
print("3 - dam para m")
print("4 - m para dm")
print("5 - dm para cm")
print("6 - cm para mm")
print("7 - mm para cm")
print("8 - cm para dm")
print("9 - dm para m")
print("10 - m para dam")
print("11 - dam para hm")
print("12 - hm para km")

escolha = input("Digite o número da conversão desejada: ")

if escolha in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
    valor = float(input("Digite o valor a ser convertido: "))
    
    if escolha in ('1', '2', '3', '4', '5', '6'):
        resultado = valor * 10
    else:
        resultado = valor / 10
    
    unidades = ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm']
    origem_index = int(escolha) - 1
    destino_index = origem_index + 1 if origem_index < 6 else origem_index - 1
    origem = unidades[origem_index]
    destino = unidades[destino_index]
    
    print(f"{valor} {origem} equivalem a {resultado} {destino}.")
else:
    print("Opção inválida!")
