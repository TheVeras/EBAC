import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

df = pd.read_csv('clientes-v3-preparado.csv')

# Categorizar Salario: acima e abaixo da mediana
df['salario_categoria'] = (df['salario']>df['salario'].median()).astype(int)

X = df[['idade','anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']]
Y = df ['salario_categoria']

# Dividir dados Treinamento e Teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar  e treinar modelo de regressão logistica
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, Y_train)

# Criar e treinar modelo de arvore de decisao
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, Y_train)

# Prever valores de teste
Y_prev_lr = modelo_lr.predict(X_test)
Y_prev_dt = modelo_dt.predict(X_test)

# Métricas de Avaliação - Regressão Logística
accuracy_lr = accuracy_score(Y_test, Y_prev_lr)
precision_lr = precision_score(Y_test, Y_prev_lr)
recall_lr = recall_score(Y_test, Y_prev_lr)

print(f'Acurácia de Regressão Logística: {accuracy_lr:.2f}')
print(f'Precisão de Regressão Logística: {precision_lr:.2f}')
print(f'Recall (sensibilidade)  de Regressão Logística: {recall_lr:.2f}')

# Métricas de Avaliação - Árvore de Decisão
accuracy_dt = accuracy_score(Y_test, Y_prev_dt)
precision_dt = precision_score(Y_test, Y_prev_dt)
recall_dt = recall_score(Y_test, Y_prev_dt)

print(f'Acurácia de Regressão Logística: {accuracy_dt:.2f}')
print(f'Precisão de Regressão Logística: {precision_dt:.2f}')
print(f'Recall (sensibilidade)  de Regressão Logística: {recall_dt:.2f}')

# Salvando o Modelo treinado
joblib.dump(modelo_lr, 'modelo_regressao_logistica.pkr')
joblib.dump(modelo_dt, 'modelo_arvore_decisao.pkr')
