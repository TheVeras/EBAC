import requests
import pandas as pd

url = 'https://query1.finance.yahoo.com/v8/finance/chart/^BVSP?interval=1d&range=1mo'

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
data = response.json()

timestamps = data['chart']['result'][0]['timestamp']
quotes = data['chart']['result'][0]['indicators']['quote'][0]

df = pd.DataFrame(quotes)
df['timestamp'] = pd.to_datetime(timestamps, unit='s')
df.set_index('timestamp', inplace=True)

print(df.head())