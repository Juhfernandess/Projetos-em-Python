import pandas as pd 
from sklearn.neighbors import NearestNeighbors
import random

# Passo 1: Coleta de preferências do usuário
print("Por favor, responda às perguntas para que possamos recomendar filmes para você:")

# Perguntas sobre preferências
genero = input("Qual gênero de filme você prefere? (Ação, Comédia, Drama, Romance): ").strip().lower()
classificacao = input("Qual a sua faixa de classificação etária preferida? (Livre, +10, +12, +16): ").strip().upper()
duracao = input("Você prefere filmes curtos ou longos? (Curto, Longo): ").strip().lower()
assunto = input("Prefere filmes sobre o que? (Tecnologia, Política, Amor, Família): ").strip().lower()
diretor = input("Você tem algum diretor favorito? (Ex: Spielberg, Tarantino, Christopher Nolan): ").strip().lower()

# Passo 2: Criação de um conjunto de dados fictício com filmes
# Aqui criamos um dataset fictício de filmes
data = {
    'Filme': ['Homem Aranha', 'Jurrasic Park', 'De repente 30', 'Interstelar', 'divertidamente', 'Marley & Eu', 'As Branquelas', 'A Culpa é das estrelas', 'Auto da Compadecida', 'Velozes e Furiosos'],
    'Gênero': ['ação', 'comédia', 'drama', 'ação', 'romance', 'comédia', 'drama', 'romance', 'comédia', 'ação'],
    'Classificação': ['Livre', '+10', '+12', '+12', '+16', 'Livre', '+10', '+12', '+10', '+16'],
    'Duração': ['longo', 'curto', 'longo', 'longo', 'curto', 'curto', 'longo', 'curto', 'longa', 'curto'],
    'Assunto': ['tecnologia', 'amor', 'família', 'política', 'tecnologia', 'amor', 'família', 'política', 'família', 'tecnologia'],
    'Diretor': ['spielberg', 'tarantino', 'nolan', 'tarantino', 'spielberg', 'nolan', 'spielberg', 'tarantino', 'nolan', 'tarantino'],
}

df = pd.DataFrame(data)

# Passo 3: Codificando as respostas do usuário (pré-processamento)
user_data = {
    'Gênero': genero,
    'Classificação': classificacao,
    'Duração': duracao,
    'Assunto': assunto,
    'Diretor': diretor
}

# Convertendo as respostas em um formato numérico para comparação (simplesmente para este exemplo)
df_encoded = df.copy()

# Vamos criar um método simples de codificação para cada coluna, aqui, apenas para fins didáticos
df_encoded['Gênero'] = df_encoded['Gênero'].apply(lambda x: 1 if x == genero else 0)
df_encoded['Classificação'] = df_encoded['Classificação'].apply(lambda x: 1 if x == classificacao else 0)
df_encoded['Duração'] = df_encoded['Duração'].apply(lambda x: 1 if x == duracao else 0)
df_encoded['Assunto'] = df_encoded['Assunto'].apply(lambda x: 1 if x == assunto else 0)
df_encoded['Diretor'] = df_encoded['Diretor'].apply(lambda x: 1 if x == diretor else 0)

# Passo 4: Treinamento de um modelo de recomendação simples (filtragem colaborativa)
# Utilizando NearestNeighbors para encontrar filmes mais similares
knn = NearestNeighbors(n_neighbors=3, metric='cosine')  # usaremos a distância do cosseno
knn.fit(df_encoded.drop('Filme', axis=1))

# Usando as respostas do usuário para encontrar filmes similares
user_vector = [[1 if x == user_data[k] else 0 for k, x in user_data.items()]]
distances, indices = knn.kneighbors(user_vector)

# Passo 5: Exibir as recomendações
print("\nRecomendações de filmes baseadas nas suas preferências:")

for i in indices[0]:
    print(df['Filme'][i])
