# https://finance.yahoo.com/quote/%5EBVSP/history/
import requests as re
from bs4 import BeautifulSoup
import pandas as pd

header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
}

response = re.get('https://finance.yahoo.com/quote/%5EBVSP/history/', headers=header)
print(response.text[:600])

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print('Pandas: ')
url_dados = pd.read_html(response.text)
print(url_dados[0].head(10))
