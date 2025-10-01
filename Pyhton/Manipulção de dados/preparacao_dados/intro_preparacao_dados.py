# Análise Exploratória de Dados(AED)
import pandas as pd

df = pd.read_csv('clientes-v2.csv')
#Verifique os primeiro e os ultimos registros pra ve se há um padrão
print(df.head().to_string())
print(df.tail().to_string())
#alterando o formato da data pra Dia/Mes/Ano
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verioficação inicial: ')
print(df.info())

print('Análise de Dados Nulos: \n', df.isnull().sum())
print('% de dados nulos: \n', df.isnull().mean()*100)
df.dropna(inplace=True)
print('Confirmar exclusão de dados nulos:\n', df.isnull().sum().sum())

print('Análise de dados duplicados:\n', df.duplicated().sum())

print('Análise de dados únicos:\n', df.nunique())

print('Estatisticas de dados:\n', df.describe())

df = df[['idade','data','estado','salario','nivel_educacao','numero_filhos','estado_civil','area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)
