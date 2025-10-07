from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import numpy as np

# Lendo o arquivo csv
df = pd.read_csv('ecommerce_estatistica.csv')

# Garantindo que Qtd_Vendidos não é um texto
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce').fillna(0)

# Criando o campo Receita = Preço * Quantidade
df['Receita'] = df['Preço'] * df['Qtd_Vendidos']

top_marcas = df.groupby('Marca')['Qtd_Vendidos'].sum().nlargest(5)

def cria_graficos(df):
    # Gráfico de Histograma - Distribuição de Notas
    histograma = px.histogram(
        df,
        x='Nota',
        nbins=10,  # <-- CORRETO no plotly
        color_discrete_sequence=['green']
    )
    histograma.update_layout(
        title='Distribuição de Notas',
        xaxis_title='Nota',
        yaxis_title='Frequência'
    )

    # Gráfico de dispersão - Número de Avaliações x Nota
    dispersao = px.scatter(
        df,
        x='N_Avaliações',
        y='Nota',
        color='Gênero',
        size='Qtd_Vendidos',
        hover_name='Título',
        size_max=60,
        opacity=0.7,
        title='Relação entre Avaliações e Nota por Gênero do Produto'
    )

    # Mapa de calor - Correlação entre variáveis numéricas
    corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos']].corr()
    calor = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale='RdBu',
        zmin=-1,
        zmax=1,
        title='Mapa de Calor - Correlação'
    )

    # Gráfico de barra - Top 5 Marcas
    barra = px.bar(
        x=top_marcas.values,
        y=top_marcas.index,
        orientation='h',
        color_discrete_sequence=px.colors.qualitative.Bold,
        title='Top 5 Marcas Mais Vendidas'
    )
    barra.update_layout(
        xaxis_title='Quantidade Vendida',
        yaxis_title='Marca',
        plot_bgcolor='rgba(255,255,255,0.8)',
        paper_bgcolor='rgba(186,245,241,1)'
    )

    # Gráfico de pizza - Distribuição por gênero
    genero_counts = df['Gênero'].value_counts().reset_index()
    genero_counts.columns = ['Gênero', 'Quantidade']
    pizza = px.pie(
        genero_counts,
        names='Gênero',
        values='Quantidade',
        hole=0.4,
        title='Distribuição por Gênero'
    )
    pizza.update_traces(
        pull=[0.1 if i == 0 else 0 for i in range(len(genero_counts))],
        textinfo='percent+label'
    )

    # Gráfico de densidade - Distribuição de Preços (heatmap)
    densidade = px.density_heatmap(
        df,
        x="Preço",
        nbinsx=30,
        color_continuous_scale='Viridis',
        title="Distribuição de Densidade - Preços"
    )

    return histograma, dispersao, calor, barra, pizza, densidade


def cria_app(df):
    app = Dash(__name__)
    histograma, dispersao, calor, barra, pizza, densidade = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=histograma),
        dcc.Graph(figure=dispersao),
        dcc.Graph(figure=calor),
        dcc.Graph(figure=barra),
        dcc.Graph(figure=pizza),
        dcc.Graph(figure=densidade)
    ])
    return app


if __name__ == '__main__':
    app = cria_app(df)
    app.run(debug=True, port=8050)
