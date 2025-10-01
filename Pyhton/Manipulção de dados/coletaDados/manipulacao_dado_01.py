import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

# Mostra os primeiros 2000 caracteres do HTML bruto
#print(requisicao.text[:2000])

# Usa o BeautifulSoup para formatar e mostrar os primeiros 2000 caracteres
extracao = BeautifulSoup(requisicao.text, 'html.parser')
print(extracao.prettify()[:2000])
