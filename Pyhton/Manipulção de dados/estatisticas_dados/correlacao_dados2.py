import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v3-preparado.csv')

# Uso Pandas
print('Estatistica do DataFrame: \n', df.describe())

print('Estatística de um Campo: \n', df[['salario', 'idade']].describe())

print('Correlação: \n', df[['salario', 'idade']].corr())
print('Correlação com Normalização: \n',df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

print('Correlação: \n', df[['salario','idadeMinMaxScaler', 'idadeStandardScaler','idadeRobustScaler']].corr())

df_filtro_idade = df[df['idade']<65]
print('Correlação de Cliente menores de 65 anos: \n', df_filtro_idade[['salario', 'idade']].corr())

# Variável espúria - aumenta com o tempo
df['Variavel_espuria'] = np.arange(len(df))

print('Variável espúria:  \n', df['Variavel_espuria'].values)

pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac','numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'Variavel_espuria']].corr()
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac','numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'Variavel_espuria']].corr(method='spearman')

print('Correlação de Pearson: \n', pearson_corr)
print('Correlação de spearman: \n', spearman_corr)
