import pandas as pd
import joblib

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v3-preparado.csv')

print(df.isnull().sum().sum())


# Carregar Modelo Treinado
modelo_regressao_linear = joblib.load('modelo_regressao_linear.pkl')
modelo_regressao_logistica = joblib.load('modelo_regressao_logistica.pkr')
modelo_arvore_decisao = joblib.load('modelo_arvore_decisao.pkr')

# Dados dos novos funcionarios
dados_novos_funcionarios = pd.DataFrame({
    'idade': [35, 45, 30],
    'anos_experiencia' : [6, 12, 5],
    'nivel_educacao_cod' : [2, 3, 4],
    'area_atuacao-cod' : [1, 4, 3]
})

# Prever o salario com mdelo treinado
salario_previsto = modelo_regressao_linear.predict(dados_novos_funcionarios)

for x in range(len(salario_previsto)):
    print(f'Salário previsto do {x+1}° funcionário: R${salario_previsto[x]:,.2f}')

# Classificar o Salario com o Modelo Treinado
categoria_salario = modelo_regressao_logistica.predict(dados_novos_funcionarios)

for x in range(len(categoria_salario)):
    categoria = 'Acima da Mediana' if categoria_salario[x] == 1 else 'Abaixo da Mediana'
    print(f'Categoria de Salário Previsto do {x+1}° funcionário: {categoria}')



