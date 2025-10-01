import pandas as pd
df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# remover dados
df.drop('pais', axis=1, inplace=True) # coluna
df.drop(2, axis=0, inplace=True) # linha

# Normalizando  campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

# converter tipos de dados
df['idade'] = df['idade'].astype(int)

print('Normalizar texto: \n', df.head())

# tratar valores nulos ausentes
df_fillna = df.fillna(0) # substitui valores nulos por 0
df_dropna = df.dropna() # remove registros com valores nulos
df_dropna4 = df.dropna(thresh=4)# manter registro com no minimo  4 valores nao nulos
df = df.dropna(subset = ['cpf'])# remover registros com cpf nulos

print('Valores nulos:\n', df.isnull().sum())
print('Quantidade de valores nulos com fillna: ',df_fillna.isnull().sum().sum())
print('Quantidade de valores nulos com dropna: ',df_dropna.isnull().sum().sum())
print('Quantidade de valores nulos com dropna4: ',df_dropna4.isnull().sum().sum())
print('Quantidade de valores nulos com CPF: ', df.isnull().sum().sum())

df.fillna({'estado':'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não Informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

# Tratar formato de Dados
df['data_corrigida'] = pd.to_datetime(df['data'], format = '%d/%m/%Y', errors = 'coerce')

# tratar dados duplicados
print('Quantidade de registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset = 'cpf', inplace = True)
print('Quantidade de registros removendo as duplicates: ',len(df))

print('Dados limpos: \n', df)

# Salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar =  df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo Dataframe: \n', pd.read_csv('clientes_limpeza.csv'))

