import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())
print(df.info())
print(df.describe)

# Garantindo que Qtd_Vendidos não é um texto
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce').fillna(0)

# Criando o campo Receita = Preço * Quantidade
df['Receita'] = df['Preço'] * df['Qtd_Vendidos']

# Gráfico de Histograma - Distribuição de Notas
plt.figure(figsize=(8, 5))
sns.histplot(df['Nota'], bins=10, kde=True, color='green')
plt.title('Distribuiução de Notas')
plt.show()

# Gráfico de dispersão - Preço X Quantidade Vendida
plt.figure(figsize=(8, 5))
plt.scatter(df['Preço'], df['Qtd_Vendidos'], alpha=0.6, color='purple')
plt.title('Disperção Preço X Vendas')
plt.xlabel('Preço')
plt.ylabel('Vendas')
plt.show()

# Mapa de calor - Correlação entra váriaveis numéricas
plt.figure(figsize=(8, 5))
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor - Correlação')
plt.show()

# Gráfico de barra
top_marcas = df.groupby("Marca")["Qtd_Vendidos"].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,6))
sns.barplot(x=top_marcas.values, hue=top_marcas.index, legend=True, palette='viridis')
plt.title('Top 5 Marcas Mais Vendidas')
plt.xlabel('Quantidade Vendida')
plt.show()

# Gráfico de pizza
genero_counts = df['Gênero'].value_counts()
plt.figure(figsize=(11,5))
plt.pie(genero_counts,labels=None, autopct="%1.1f%%", colors=sns.color_palette('Set2'))
plt.legend(
    labels=[f"{g} ({v})" for g, v in zip(genero_counts.index, genero_counts.values)],
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    title="Gênero"
)
plt.title('Distribuição Por Gênero')
plt.show()

# Gráfico de densidade
plt.figure(figsize=(8,6))
sns.kdeplot(df["Preço"], fill=True, color="red")
plt.title("Gráfico de Densidade - Preço")
plt.xlabel("Preço")
plt.show()

# Gráfico de Regressão
plt.figure(figsize=(8,6))
sns.regplot(x="Preço", y="Qtd_Vendidos", data=df, scatter_kws={"alpha":0.5}, line_kws={"color":"blue"})
plt.title("Regressão - Preço vs Vendas")
plt.show()
