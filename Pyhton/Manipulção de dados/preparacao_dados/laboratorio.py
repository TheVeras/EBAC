import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
# Carregando os dados
df = pd.read_csv('/data/ecommerce_tratados.csv')

print(df.info())

# 1. Verificar a quantidade de dados únicos para cada campo
# Dica: Use o método que retorna o número de valores únicos por coluna
# Armazene o resultado na variável 'unicos'
unicos = df.nunique()

# 2. Verificar as estatísticas dos campos numéricos
# Dica: Use o método que gera estatísticas descritivas (média, desvio, min, max, etc.)
# Armazene o resultado na variável 'estatisticas'
estatisticas = df.describe()
# 3. Criar o campo 'Preco' com o cálculo: Reais + (Centavos/100)
# Dica: Acesse as colunas 'Reais' e 'Centavos' do DataFrame
# Lembre-se de dividir os centavos por 100 para converter para formato decimal
df['Preco'] = df['Reais'] + (df['Centavos']/100)

# 4. Remover os seguintes campos: ['Reais', 'Centavos', 'Condicao', 'Condicao_Atual']
# Dica: Use o método drop() com o parâmetro columns
# Não esqueça de atribuir o resultado de volta ao DataFrame
df = df.drop(['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'], axis=1)

# Verificação dos resultados - NÃO ALTERE ESTA PARTE
print("Dados Únicos por Campo:")
print(unicos)

print("\nEstatísticas dos Campos Numéricos:")
print(estatisticas)

print("\nDataFrame após as alterações:")
print(df.head())

# Instanciar os escaladores e codificadores
# Dica: Crie uma instância de cada classe importada
min_max_scaler = MinMaxScaler()
label_encoder = LabelEncoder()
# Definir nomes das colunas (para evitar erros de digitação)
nome_coluna_n_avaliacoes = 'N_Avaliacoes'
nome_coluna_preco = 'Preco'

# 1. Criar o campo Nota_MinMax com normalização MinMax da coluna 'Nota'
# Dica: Use fit_transform() do MinMaxScaler. Atenção: a entrada deve ser 2D (use [['coluna']])
df['Nota_MinMax'] = min_max_scaler.fit_transform(df[['Nota']])

# 2. Criar o campo N_Avaliacoes_MinMax com normalização MinMax da coluna 'N_Avaliacoes'
# Dica: Use a variável nome_coluna_n_avaliacoes e lembre-se dos colchetes duplos
df['N_Avaliacoes_MinMax'] = min_max_scaler.fit_transform(df[[nome_coluna_n_avaliacoes]])

# 3. Criar o campo Desconto_MinMax com normalização MinMax da coluna 'Desconto'
# Dica: Mesmo padrão dos anteriores
df['Desconto_MinMax'] = min_max_scaler.fit_transform(df[['Desconto']])

# 4. Criar o campo Preco_MinMax com normalização MinMax da coluna 'Preco'
# Dica: Use a variável nome_coluna_preco
df['Preco_MinMax'] = min_max_scaler.fit_transform(df[[nome_coluna_preco]])

# 5. Criar o campo Marca_Cod usando LabelEncoder na coluna 'Marca'
# Dica: LabelEncoder trabalha com dados 1D, então use apenas ['Marca'] (colchetes simples)
df['Marca_Cod'] = label_encoder.fit_transform(df['Marca'])

# 6. Criar o campo Material_Cod usando LabelEncoder na coluna 'Material'
# Dica: Mesmo padrão do anterior
df['Material_Cod'] = label_encoder.fit_transform(df['Material'])
# 7. Criar o campo Temporada_Cod usando LabelEncoder na coluna 'Temporada'
# Dica: Mesmo padrão dos dois anteriores
df['Temporada_Cod'] = label_encoder.fit_transform(df['Temporada'])

# Verificação dos resultados - NÃO ALTERE ESTA PARTE
print("DataFrame após as transformações:")
print(df.head())


# 1. Criar função para transformar Qtd_Vendidos em códigos numéricos
def transform_qtd_vendidos(qtd):
    """
    Transforma strings de quantidade vendida em valores numéricos
    """
    # Complete a função seguindo o padrão:
    # 'Nenhum' -> 0, '1' -> 1, '2' -> 2, etc.
    # Para valores como '+5', '+25', use apenas o número (5, 25)
    # Para '+10mil' -> 10000, '+50mil' -> 50000

    if qtd == 'Nenhum':
        return 0
    elif qtd == '1':
        return 1
    elif qtd == '2':
        return 2
    elif qtd == '3':
        return 3
    elif qtd == '4':
        return 4
    elif qtd == '+5':
        return 5
    elif qtd == '+25':
        return 25
    elif qtd == '+50':
        return 50
    elif qtd == '+100':
        return 100
    elif qtd == '+1000':
        return 1000
    elif qtd == '+10mil':
        return 10000
    elif qtd == '+50mil':
        return 50000
    else:
        return None


# Aplicar a função na coluna Qtd_Vendidos para criar Qtd_Vendidos_Cod
# Dica: Use o método apply() para aplicar uma função a cada elemento da coluna
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].apply(transform_qtd_vendidos)

# 2. Criar o campo Marca_Freq com proporção de frequência da Marca
# Primeiro: calcular a frequência de cada marca dividida pelo total de linhas
# Dica: Use value_counts() para contar e divida por len(df)
marca_freq = df['Marca'].value_counts() / len(df)

# Depois: mapear essas frequências de volta para o DataFrame
# Dica: Use o método map() para substituir cada marca por sua frequência
df['Marca_Freq'] = df['Marca'].map(marca_freq)

# 3. Criar o campo Material_Freq com proporção de frequência do Material
# Dica: Siga o mesmo padrão usado para Marca_Freq
material_freq = df['Material'].value_counts() / len(df)
df['Material_Freq'] = df['Material'].map(material_freq)

# Verificação dos resultados - NÃO ALTERE ESTA PARTE
print("DataFrame após as transformações:")
print(df.head())