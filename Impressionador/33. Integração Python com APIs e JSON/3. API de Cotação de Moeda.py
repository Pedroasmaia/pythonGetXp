import requests as r
import json

cotacoes = r.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()
print(f"Dolar: {cotacoes_dic['USD']['bid']}")
print(f"Euro: {cotacoes_dic['EUR']['bid']}")
print(f"Bitcoin: {cotacoes_dic['BTC']['bid']}")

cotacoes_30days = r.get("https://economia.awesomeapi.com.br/json/daily/USD/30")
cotacoes_30days_dic = cotacoes_30days.json()
dollar_30days = [float(item['bid']) for item in cotacoes_30days_dic]
print(dollar_30days)