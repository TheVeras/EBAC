import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}

    # Pegando o título
    titulo = artigo.h3.a['title']
    livro['Título'] = titulo

    # Pegando o preço
    preco = artigo.find('p', class_='price_color').text
    livro['Preço'] = preco

    # Adiciona o livro no catálogo
    catalogo.append(livro)

    # Conta mais um livro
    contar_livros += 1

print('Total livros:', contar_livros)

# Opcional: mostrar o catálogo como tabela
df = pd.DataFrame(catalogo)
print(df)

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# requests.packages.urllib3.disable_warnings()
#
# url = 'https://books.toscrape.com/'
# requisicao = requests.get(url)
# requisicao.encoding = 'utf-8'
#
# extracao = BeautifulSoup(requisicao.text, 'html.parser')
#
# contar_livros = 0
# catalogo = []
#
# for artigo in extracao.find_all('article', class_='product_pod'):
#     livro = {}
#
#     # Primeiro for: título
#     for h3 in artigo.find_all('h3'):
#         titulo = h3.a['title']
#         livro['Título'] = titulo
#
#     # Segundo for: preço
#     for p in artigo.find_all('p', class_='price_color'):
#         preco = p.text
#         livro['Preço'] = preco
#
#     catalogo.append(livro)
#     contar_livros += 1

