import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}
url = 'https://python.org.br/web/'
requisicao = requests.get(url,headers=headers)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Exibir texto
#(extracao.text.strip())

# Filtrando a exibição pela tag
# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
#     print('Titulo', titulo)
#
# # contando h2 e h3
# cont_titulo = 0
# cont_subtitulo = 0
#
# for linha_texto in extracao.find_all((['h2','h3'])):
#     if linha_texto.name == 'h2':
#         cont_titulo += 1
#     elif  linha_texto.name == 'h3':
#         cont_subtitulo += 1
#
# print(f'Total de titulo: {cont_titulo}')
# print(f'Total de Subtitulos: {cont_subtitulo}')

for titulo in extracao.find_all('h2'):
    print('\n Título: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(),' | URL: ', a['href'])
