import requests
import json
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
#print (cotacoes)
cotacao_dolar = cotacoes['USDBRL']['bid']
print (cotacao_dolar)