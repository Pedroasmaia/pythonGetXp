import requests as r
import matplotlib.pyplot as plt
import json


cotacoes = r.get("https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20230101&end_date=20231031")
cotacoes_dic = cotacoes.json()
cotacoes_list = [float(item['bid']) for item in cotacoes_dic]
print(f"Quantidade de cotações: {len(cotacoes_list)}")
cotacoes_list.reverse()
plt.figure(figsize=(15,5))
plt.plot(cotacoes_list)
plt.show()