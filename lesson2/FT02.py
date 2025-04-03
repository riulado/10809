import pandas as pd
import matplotlib.pyplot as plt

# 1-Carregamento e Exploração Inicail
df_conjunto = pd.read_csv('02 uber_reviews_without_reviewid.csv')

# Mostra detalhes das colunas (número de entraddas não nulas, tipo de dados).
print(df_conjunto.info())

# Exibe as primeiras 5 linhas para visualizar os daddos reais e identificar 
# possíveis problemas ou padrões.
print(df_conjunto.head())

# 2 - Limpeza de Dados
# 2.1 - Remover a coluna userImage
"""A coluna 'userImage' não contém valores úteis (todos são nulos). 
Manter colunas irrelevantes aumenta a complexidade da análise 
e consome memória desnecessariamente."""
df_cleaned = df_conjunto.drop(columns=['userImage'])

print(df_cleaned.info())
print(df_cleaned.head())

# 2.2 - Preencher valores ausentes
"""Colunas como reciewCreatedVersion e appVersion têm valores ausentes (~1740 registos). 
Preencher com 'Desconhecida' permite a integridade do dataset, evitanto erros em análises futuras.

Preencher valores ausentes é uma prática comum para evitar perda de dados durante operções
(ex: agragações, filtragem)."""
print(df_cleaned.fillna({'reviewCreatedVersion': 'Desconhecida'}, inplace=True))
print(df_cleaned.fillna({'appVersion': 'Desconhecida'}, inplace=True))

# 3 - Análise Descritiva
# 3.1 - Distribuição de avaliações(score)
"""Saber a frequência de cada pontuação """
print(df_cleaned['score'].value_counts())

# 3.2 - Resumo de "thumbsUpCount" (gostos)
print(df_cleaned['thumbsUpCount'].describe())

# 4 - Distribuição Temporal das Análises
df_cleaned['at'] = pd.to_datetime(df_cleaned['at'])
print(df_cleaned['at'].dt.year.value_counts().sort_index().head())

# 5 - Resumo de Respostas
print(df_cleaned[['replyContent', 'repliedAt']].dropna().head())

print(df_cleaned[['replyContent', 'repliedAt']].dropna().head())

# 6 - Correlação entre score e thumbsUpCount
print(df_cleaned[['score', 'thumbsUpCount']].corr())

# 7 - Visualiazação
print(df_cleaned['score'].value_counts().plot(kind='bar', title='Distribuição de Avaliações'))

# 8 - Exportação do DataFrame Limpo
df_cleaned.to_csv('uber_reviews_cleaned.csv', index=False)
