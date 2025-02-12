# Leitura do primeiro termo e da razão
print("-----BEM-VINDO AO CÁLCULO DE P.A. INTERATIVO-----")
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializando variáveis
termo = primeiro_termo
contador = 1
total_termos = 10  # Começanado com 10 termos

# Loop principal para exibir os termos da PA
while total_termos != 0:
    for _ in range(total_termos):
        print(termo, end=" → ")
        termo += razao
        contador += 1
    print("PAUSA")

    # Pergunta quantos termos adicionais o usuário quer ver
    total_termos = int(input("\nQuantos termos a mais você quer mostrar? (Digite 0 para sair): "))

print("Progressão finalizada! ")
