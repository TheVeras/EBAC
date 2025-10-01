import pandas as pd
import numpy as np

df = pd.read_csv('/data/ecommerce.csv')

# Verifique a quantidade de linhas e colunas
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# Verifique os tipos de dados
tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

# Verifique a quantidade de valores nulos
nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

#  Substitua os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’
df['Temporada'] = df['Temporada'].fillna('Não Definido')
df.fillna({'Marca':'Não Definido'},inplace=True)

# Converter a coluna 'Marca' para letras minúsculas
df['Marca'] = df['Marca'].str.lower()

# Converter a coluna 'Material' para letras minúsculas
df['Material'] = df['Material'].str.lower()

# Converter a coluna 'Temporada' para letras minúsculas
df['Temporada'] = df['Temporada'].str.lower()

# Remover linhas duplicadas
df.drop_duplicates()

# Remover linhas com menos de 8 valores não nulos
# O parâmetro 'thresh' define o número mínimo de valores não nulos necessários para manter a linha
df.dropna(thresh=8, inplace=True)

# Calcular o intervalo interquartil (IQR)
q1 = df['N_Avaliacoes'].quantile(0.25)
q3 = df['N_Avaliacoes'].quantile(0.75)
iqr = q3-q1

# Definir o limite superior para identificar outliers
limite_alto = q3 + 1.5 * iqr

# Filtrar os produtos que possuem um número de avaliações maior que o limite superior
df_avaliados = df[(df['N_Avaliacoes'] >= limite_alto)]

# Extrair e limpar os dados da coluna 'Condicao'
# A função lambda é usada aqui para pegar a primeira palavra da string na coluna 'Condicao'
# x.split(' ')[0] pega a primeira palavra da string.
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split('|')[0].strip())

# A função lambda é usada aqui para pegar a quinta palavra da string na coluna 'Condicao' se existir,
# caso contrário, retorna 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(
    lambda x: x.split(' ')[4].strip() if len(x.split(' ')) > 3 else 'Nenhum'
)

# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)
# A função lambda é usada aqui para remover o símbolo '%' da string na coluna 'Desconto'
df['Desconto'] = df['Desconto'].apply(lambda x: str(x).split('%')[0] if pd.notna(x) else np.nan)