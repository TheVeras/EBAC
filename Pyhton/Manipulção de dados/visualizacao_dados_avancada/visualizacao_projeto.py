import plotly.express as px
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

# Mapa de calor interativo de correlações
df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
fig = px.imshow(df_corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Mapa de Calor de Correlação')
fig.show()

# Área Plot do Salário ao Longo da Idade
fig = px.area(df,x='idade', y='salario', line_group='estado_civil', color='estado_civil', title='Evolução do Sálario por Idade e Estado Civil')
fig.show()

# Visualização dos Resultados dos Modelos de Classificação e Regressão

# Gráficos para a Classificação
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Matriz de Confusão para Regressão Logística
cm_lr = confusion_matrix(Y_test, Y_prev_lr)
plt.figure(figsize=(8,6))
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Matriz de Confusão: Regressão Logística')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()

# Matriz de Confusão para Àrvore de Decisão
cm_dt = confusion_matrix(Y_test, Y_prev_dt)
plt.figure(figsize=(8,6))
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title('Matriz de Confusão - Àrvore de Decisão')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()

# Gráfico para Regressão Linear
import matplotlib.pyplot as plt

# Plot de Regressão
plt.figure(figsize=(10,6))
plt.sacatter(Y_test, Y_prev, alpha=0.5)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'k--', lw=4)
plt.title('Valores Reais vs Predições: Regressão Linear')
plt.xlabel('Real')
plt.ylabel('Previsto')
plt.show()

# Visualização da Correlção
import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap de Correlação Pearson
plt.figure(figsize=(10,8))
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação de Pearson entre Variáveis')
plt.show()

# Heatmap de Correlação Spearman
plt.figure(figsize=(10,8))
sns.heatmap(spearman_corr, annot=True, cmap='viridis', fmt=".2f")
plt.title('Correlação de Spearman entre Variáveis')
plt.show()


import plotly.express as px

# Visualização interativa usando plotly para correlação de Pearson
fig = px.imshow(pearson_corr, text_auto=True, aspect="auto", color_cotinuous_scale='RdBu', title='Correlação de Pearson Interativa')
fig.show()

# Visualização interativa usando plotly para correlação de Spearman
fig = px.imshow(spearman_corr, text_auto=True, aspect="auto", color_cotinuous_scale='RdBu', title='Correlação de Spearman Interativa')
fig.show()
