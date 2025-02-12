import random
import string

def gerar_senha(longitude=12, dica=""):
    # Conjunto de caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Embaralha a dica do usuário e adiciona caracteres aleatórios
    dica_embaralhada = "".join(random.sample(dica, len(dica))) if dica else ""
    restante = "".join(random.choices(caracteres, k=longitude - len(dica_embaralhada)))

    # Mistura a dica embaralhada com os outros caracteres
    senha = list(dica_embaralhada + restante)
    random.shuffle(senha)
    
    return "".join(senha)

# Pergunta ao usuário se ele quer uma dica na senha
print("===== GERADOR DE SENHAS SEGURAS =====")
dica_usuario = input("Digite uma palavra ou algo para ajudar a lembrar da senha (ou pressione Enter para ignorar): ").strip()

# Gera e exibe a senha segura
senha_segura = gerar_senha(dica=dica_usuario)
print("\nSua senha gerada é: " + senha_segura)
print("DICA: Anote-a em um local seguro!")
    